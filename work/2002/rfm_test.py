import pandas as pd

TIME = '2019-07-1'

# 1 数据概览
df_origin = pd.read_excel('D:\Code\DA-cases-master\RFM\PYTHON-RFM实战数据.xlsx')
# print(df_origin.head())

# 1.1 查看交易状态
# print(df_origin['订单状态'].unique())  # ['交易成功' '付款以后用户退款成功，交易自动关闭']

# 1.2 查看数据类型
# print(df_origin.info())

# 2 数据清洗
# 2.1 剔除退款
df = df_origin.loc[df_origin['订单状态'] == '交易成功', :]
# print(df.head())

# 2.2 关键字段提取
df = df[['买家昵称', '付款日期', '实付金额']]
# print(df.head())

# 2.3 R值构造
r = df.groupby('买家昵称')['付款日期'].max().reset_index()  # 取每个买家最后一次购买日期
# print(r.head())
r['R'] = (pd.to_datetime(TIME) - r['付款日期']).dt.days
r = r[['买家昵称', 'R']]
# print(r)

# 2.4 F值构造
# 引入日期标签辅助列
df['日期标签'] = df['付款日期'].astype(str).str[:10]  # 切片保留到日期到天

# 把单个用户一天内订单合并
dup_f = df.groupby(['买家昵称', '日期标签'])['付款日期'].count().reset_index()
# print(dup_f.head())

# 对合并后的用户统计频次
f = dup_f.groupby('买家昵称')['付款日期'].count().reset_index()
f.columns = ['买家昵称', 'F']
# print(f.head())

# 2.5 M值构造
sum_m = df.groupby('买家昵称')['实付金额'].sum().reset_index()
sum_m.columns = ['买家昵称', '总支付金额']
com_m = pd.merge(sum_m, f, left_on='买家昵称', right_on='买家昵称', how='inner')

# 计算用户平均支付金额
com_m['M'] = com_m['总支付金额'] / com_m['F']  # 总订单金额➗订单数
# print(com_m.head())

# 2.6 合并三值
rfm = pd.merge(r, com_m, left_on='买家昵称', right_on='买家昵称', how='inner')
rfm = rfm[['买家昵称', 'R', 'F', 'M']]
# print(rfm.head())

# 3 分值计算
# 3.1 R值计算
# 对最后购买日期按档分类,[0,30)为5，[30,60)为4 ......
rfm['R-SCORE'] = pd.cut(rfm['R'], bins=[0, 30, 60, 90, 120, 1000000], labels=[5, 4, 3, 2, 1], right=False).astype(float)
# print(rfm)

# 3.2 F、M值计算
rfm['F-SCORE'] = pd.cut(rfm['F'], bins=[1, 2, 3, 4, 5, 1000000], labels=[1, 2, 3, 4, 5], right=False).astype(float)
rfm['M-SCORE'] = pd.cut(rfm['M'], bins=[0, 50, 100, 150, 200, 1000000], labels=[1, 2, 3, 4, 5], right=False).astype(float)

# 3.3 对比平均值，减少分类数量
# 大于平均值为1，小于平均值为0，减少分类数量至8个
rfm['R是否大于均值'] = (rfm['R-SCORE'] > rfm['R-SCORE'].mean()) * 1
rfm['F是否大于均值'] = (rfm['F-SCORE'] > rfm['F-SCORE'].mean()) * 1
rfm['M是否大于均值'] = (rfm['M-SCORE'] > rfm['M-SCORE'].mean()) * 1
rfm.head()

# 4 客户分层
# 4.1 构建合并指标
rfm['人群数值'] = (rfm['R是否大于均值'] * 100) + (rfm['F是否大于均值'] * 10) + (rfm['M是否大于均值'] * 1)  # 构建真值表


# 4.2 基于指标给客户打标签
def transform_label(x):
    label = None
    if x == 111:
        label = '重要价值客户'
    elif x == 110:
        label = '消费潜力客户'
    elif x == 101:
        label = '频次深耕客户'
    elif x == 100:
        label = '新客户'
    elif x == 11:
        label = '重要价值流失预警客户'
    elif x == 10:
        label = '一般客户'
    elif x == 1:
        label = '高消费唤回客户'
    elif x == 0:
        label = '流失客户'
    return label


rfm['人群类型'] = rfm['人群数值'].apply(transform_label)

# 5 统计输出
# 5.1 人数统计
count = rfm['人群类型'].value_counts().reset_index()
count.columns = ['客户类型', '人数']
count['人数占比'] = count['人数'] / count['人数'].sum()

# 5.2 金额统计
rfm['购买总金额'] = rfm['F'] * rfm['M']
mon = rfm.groupby('人群类型')['购买总金额'].sum().reset_index()
mon.columns = ['客户类型', '消费金额']
mon['金额占比'] = mon['消费金额'] / mon['消费金额'].sum()

result = pd.merge(count, mon, left_on='客户类型', right_on='客户类型')
print(result)
print(rfm)
