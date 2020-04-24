import pandas as pd
import numpy as np

pd.set_option('mode.chained_assignment', None)

df_baoming = pd.read_csv(r'C:\Users\Healthlink\Desktop\数据\中医检测活动数据\健康管家钜献-2019-08-15.csv', engine='python',
                         encoding='gbk')

df_baoming_saler = pd.read_excel(r'C:\Users\Healthlink\Desktop\天津国寿中医检测活动数据空白模板.xlsx',
                                 sheet_name='客户报名')

df_baoming_user = pd.read_excel(r'C:\Users\Healthlink\Desktop\天津国寿中医检测活动数据空白模板.xlsx',
                                 sheet_name='客户转介绍')

df_saler = pd.read_excel(r'C:\Users\Healthlink\Desktop\数据\中医检测活动数据\所有备案名单0815.xlsx')

df_card = pd.read_excel(r'C:\Users\Healthlink\Desktop\数据\中医检测活动数据\天津卡激活数据提取.xls')

df_baoming = df_baoming[df_baoming['是否报名'] == '是'].fillna('')

new_baoming_saler = pd.DataFrame(data=None, index=None, columns=df_baoming_saler.columns).fillna('')
# Columns: [序号, 日期, 报名客户姓名, 手机号, 注册时间, 报名时间, 开卡时间, 营销员（邀请人）, 营销员工号, 所属公司]

new_baoming_user = pd.DataFrame(data=None, index=None, columns=df_baoming_user.columns).fillna('')
# Columns: ['序号', '日期', '客户\n报名姓名', '手机号', '注册时间', '报名时间', '开卡时间', '客户\n（邀请人）','邀请人手机号', '绑定营销员', '营销员工号', '所属公司']
print(df_saler['二级名称'][1])

def to_date(t):
    """
    2019-08-13 14:56 --> 2019年8月13日
    """
    year = t[:4]
    month = t[5:7]
    day = t[8:10]
    return '{}年{}月{}日'.format(year, month, day)

def replace_e(x):
    if x == '1' or x == 1:
        x = ' '
    return x

# sheet --> 活动报名
new_baoming_saler['日期'] = df_baoming['报名时间']
new_baoming_saler['日期'] = new_baoming_saler['日期'].transform(to_date)
new_baoming_saler['报名客户姓名'] = df_baoming['姓名']
new_baoming_saler['手机号'] = df_baoming['手机号']
new_baoming_saler['注册时间'] = df_baoming['注册时间']
new_baoming_saler['报名时间'] = df_baoming['报名时间']
df_baoming['营销员姓名'] = df_baoming['营销员姓名'].transform(replace_e)
# new_baoming_saler['营销员\n（邀请人）'] = df_baoming['邀请人']
new_baoming_saler['营销员\n（邀请人）'] = df_baoming['营销员姓名']
df_baoming['营销员工号'] = df_baoming['营销员工号'].transform(replace_e)
new_baoming_saler['营销员工号'] = df_baoming['营销员工号']

df_saler['客户经理工号'] = df_saler['客户经理工号'].astype('str')
new_baoming_saler = new_baoming_saler.reset_index(drop=True)

new_baoming_saler = new_baoming_saler.drop(new_baoming_saler[new_baoming_saler['营销员工号'].map(len) < 5].index)


def to_int(x):
    x = x[:-2]
    return x


df_saler['客户经理工号'] = df_saler['客户经理工号'].transform(to_int)

for i in range(new_baoming_saler.shape[0]):
    try:
        # print('客户经理工号:\n',df_saler['客户经理工号'])
        # print('营销员工号:\n',new_baoming_saler["营销员工号"][i])
        # print('二级名称:\n',df_saler[df_saler['客户经理工号'] == '12011382000110'].iloc[0]['二级名称'])
        # print('-'*50)
        new_baoming_saler['所属公司'][i] = df_saler[df_saler['客户经理工号'] == new_baoming_saler["营销员工号"][i]].iloc[0]['二级名称']
    except:
        # 跳过无法匹配的工号
        pass

for i in range(new_baoming_saler.shape[0]):
    try:
        # print('卡激活表：\n',df_card['用户手机号'])
        # print('报名表：\n',new_baoming_saler["手机号"])
        new_baoming_saler['开卡时间'][i] = df_card[df_card['用户手机号'] == new_baoming_saler["手机号"][i]].iloc[0]['卡激活日期']
    except:
        # 跳过无法匹配的手机号
        pass

df_baoming_saler = pd.concat([df_baoming_saler, new_baoming_saler], axis=0, ignore_index=True)
df_baoming_saler.columns = ['序号', '日期', '报名客户姓名', '手机号', '注册时间', '报名时间', '开卡时间',
       '营销员\n（邀请人）', '营销员工号', '所属公司']
df_baoming_saler['序号'] = range(1, len(df_baoming_saler) + 1)
# print(df_baoming_saler)
# sheet 活动报名 完成

# sheet 客户转介绍
new_baoming_user['日期'] = df_baoming['报名时间']
new_baoming_user['日期'] = new_baoming_saler['日期'].transform(to_date)
new_baoming_user['客户\n报名姓名'] = df_baoming['姓名']
new_baoming_user['手机号'] = df_baoming['手机号']
new_baoming_user['注册时间'] = df_baoming['注册时间']
new_baoming_user['报名时间'] = df_baoming['报名时间']
new_baoming_user['客户\n（邀请人）'] = df_baoming['邀请人']
new_baoming_user['邀请人手机号'] = df_baoming['邀请人手机号']
new_baoming_user['绑定营销员'] = df_baoming['营销员姓名']
new_baoming_user['营销员工号'] = df_baoming['营销员工号']

new_baoming_user = new_baoming_user.reset_index(drop=True)
new_baoming_user = new_baoming_user.drop(new_baoming_user[new_baoming_user['客户\n（邀请人）'].map(len) < 2].index)



for i in range(new_baoming_user.shape[0]):
    try:
        # print(df_saler[df_saler['客户经理工号'] == new_baoming_user["营销员工号"][i]].iloc[0]['二级名称'])
        new_baoming_user['所属公司'][i] = df_saler[df_saler['客户经理工号'] == new_baoming_user["营销员工号"][i]].iloc[0]['二级名称']
    except:
        # 跳过无法匹配的工号
        pass

for i in range(new_baoming_user.shape[0]):
    try:
        # print('卡激活表：\n',df_card['用户手机号'])
        # print('报名表：\n',new_baoming_user["手机号"])
        new_baoming_user['开卡时间'][i] = df_card[df_card['用户手机号'] == new_baoming_user["手机号"][i]].iloc[0]['卡激活日期']
    except:
        # 跳过无法匹配的手机号
        pass

df_baoming_user = pd.concat([df_baoming_user, new_baoming_user], axis=0, ignore_index=True)
df_baoming_user.columns = ['序号', '日期', '客户\n报名姓名', '手机号', '注册时间', '报名时间', '开卡时间', '客户\n（邀请人）',
       '邀请人手机号', '绑定营销员', '营销员工号', '所属公司']
df_baoming_user['序号'] = range(1, len(df_baoming_user) + 1)
# print(df_baoming_saler)
# sheet 活动报名 完成


writer = pd.ExcelWriter(r'C:\Users\Healthlink\Desktop\天津国寿中医检测活动数据20190814.xlsx')
df_baoming_saler.to_excel(writer, '客户报名', index=None)
df_baoming_user.to_excel(writer, '客户转介绍', index=None)
writer.save()
