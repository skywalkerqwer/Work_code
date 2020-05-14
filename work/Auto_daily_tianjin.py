# -*- coding: UTF-8 -*-
"""
    以2019-12月内蒙国寿活动为模板，生成每日报表
    天津国寿2020-01-08活动
"""

import pandas as pd
import time, datetime

t1 = time.time()

# 调整输出显示
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 5000)

# 常参
TIME = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 当日日期  2019-12-06
START_TIME = '2019-4-2 00:00:00'  # 活动开始时间
PATH = r'C:\Users\Healthlink\Desktop\日报统计数据\天津4月\数据源\\'
print('今天日期为：', TIME, '  星期', datetime.datetime.now().isoweekday(), sep='')

# 文件名称
FILE_sales = r'天津国寿营销员会议-' + str(TIME)+ ".csv"
FILE_member = r'天津国寿会员会议-' + str(TIME)+ ".csv"
FILE_sales_info = r'员工列表.csv'
FILE_card = r'天津卡激活数据提取.xls'
# FILE_error = r'12-10失效报名.xlsx'  # 21个报名未关联营销员信息补充表格

# 读取两个会议数据和营销员备案数据
print('开始读取...')
df_sales = pd.read_csv(PATH + FILE_sales, encoding='utf-8')  # 营销员会议
df_member = pd.read_csv(PATH + FILE_member, encoding="utf-8")  # 会员会议
df_info = pd.read_csv(PATH + FILE_sales_info, engine='python')  # 营销员备案
df_card = pd.read_excel(PATH + FILE_card)  # 卡激活信息
# df_error = pd.read_excel(PATH + FILE_error, encoding='utf-8')  # 补充表
t2 = time.time()
print('读取完成，耗时%.2fs' % (t2-t1))


# 处理员工列表信息
def replace_c(x):  # 移除逗号comma
    x = str(x)
    x = x.replace(',', '')
    x = x.replace('，', '')
    return x


df_info['客户经理工号'] = df_info['客户经理工号'].fillna(0)
df_info['客户经理工号'] = df_info['客户经理工号'].apply(replace_c)
df_info['客户经理工号'] = df_info['客户经理工号'].astype('int64')

# 处理卡激活信息
df_card['卡激活日期'] = df_card['卡激活日期'].astype('datetime64')  # 修改日期格式
df_cheat_card = df_card[df_card['用户手机号'].isnull()]
df_cheat_card = df_cheat_card.reset_index(drop=True)  # 务必重置索引！否则merge后无法修改数据
df_card = df_card.sort_values('卡激活日期', ascending=False)  # 按卡激活日期倒序
df_card = df_card[df_card['卡激活日期'] >= START_TIME]  # 筛选活动开始后的卡激活信息
df_card = df_card.fillna(0)  # 处理NA
df_card['用户手机号'] = df_card['用户手机号'].astype('int64')  # 统一手机号数据类型
df_card['营销员工号'] = df_card['营销员工号'].astype('int64')  # 统一手机号数据类型
df_card = df_card.drop_duplicates(subset='用户手机号', keep='first')  # 一人多次开卡存在重复项，进行去重
df_card = df_card.reset_index(drop=True)  # 重置索引
# print("df_sales['手机号'].dtypes:", df_sales['手机号'].dtypes)  # int64
# print("df_card['用户手机号'].dtypes:", df_card['用户手机号'].dtypes)  # float64
# print("df_member['手机号'].dtypes:", df_member['手机号'].dtypes)  # int64
# print(df_card)

# 创建三个sheet页对应的df
df_first = pd.DataFrame(columns=['报名日期', '客户姓名', '客户手机号', '卡产品名称', '卡激活日期', '绑定营销员', '绑定营销员工号', '所属机构'])
df_second = pd.DataFrame(columns=['报名日期', '一级客户姓名', '一级客户手机号', '转介绍客户姓名', '转介绍客户手机号', '卡产品名称', '卡激活日期', '绑定营销员', '绑定营销员工号', '所属机构'])
df_third = pd.DataFrame(columns=["客户姓名", '客户手机号', '绑定营销员', '绑定营销员工号', '所属机构', '所属职场','邀请激活人数'])
df_invalid = pd.DataFrame(columns=['报名日期', '客户姓名', '客户手机号', '卡产品名称', '卡激活日期', '绑定营销员', '绑定营销员工号', '所属机构'])

# 处理会议数据
# 营销员会议
df_sales = df_sales[df_sales['是否报名'] == '是']  # 筛选一级报名客户
df_sales = df_sales.sort_values('报名时间', ascending=False)  # 按报名时间倒序
df_sales = df_sales.reset_index(drop=True)  # 倒序后重置索引
# arr = range(len(df_sales)-21, len(df_sales))  # 获取最后错误的21行的索引
# df_sales = df_sales.drop(arr, axis=0)  # 删除原表中最后错误的21行
# df_sales = pd.concat([df_sales, df_error])  # 用正确的21行填充
# df_sales = df_sales.reset_index(drop=True)  # 重置索引

# 会员会议
df_member = df_member[df_member['是否报名'] == '是']  # 筛选二级报名客户
df_member = df_member.sort_values(['报名时间'], ascending=False)  # 按报名时间倒序
df_member = df_member.reset_index(drop=True)  # 倒序后重置索引


# 处理第一张报名表
# print('开始处理:<报名表>...')
df_first['报名日期'] = df_sales['报名时间']
df_first["客户姓名"] = df_sales['姓名']
df_first["客户手机号"] = df_sales['手机号']
sales_card = pd.merge(df_sales, df_card, how='left', left_on='手机号', right_on='用户手机号')  # 按手机号匹配营销员会议开卡信息
# print(sales_card)
df_first["卡产品名称"] = sales_card['卡产品名称']
df_first["卡激活日期"] = sales_card['卡激活日期']
df_first["绑定营销员"] = df_sales['邀请报名人']
sales_info = pd.merge(df_sales, df_info, how="left", left_on='邀请报名人手机号', right_on='手机号')  # 按营销员手机号匹配备案信息
df_first['绑定营销员工号'] = sales_info['客户经理工号']
df_first["所属机构"] = sales_info['二级名称']
df_first["所属职场"] = sales_info['三级名称']
# df_first['序号'] = range(1, len(df_first)+1)  # 写入序号
print('完成处理：<报名表>')

# 处理第二张转介绍表
# print('开始处理:<转介绍表>...')
df_second['报名日期'] = df_member['报名时间']
df_second['转介绍客户姓名'] = df_member["姓名"]
df_second["转介绍客户手机号"] = df_member['手机号']
df_second['一级客户姓名'] = df_member["邀请报名人"]
df_second["一级客户手机号"] = df_member['邀请报名人手机号']
member_card = pd.merge(df_member, df_card, how='left', left_on='手机号', right_on='用户手机号')
df_second['卡产品名称'] = member_card['卡产品名称']
df_second['卡激活日期'] = member_card["卡激活日期"]
member_sales = pd.merge(df_member, df_first, how='left', left_on="邀请报名人手机号", right_on='客户手机号')
# print(member_sales)
df_second["绑定营销员"] = member_sales['绑定营销员']
df_second['绑定营销员工号'] = member_sales['绑定营销员工号']
df_second["所属机构"] = member_sales['所属机构']
df_second["所属职场"] = member_sales['所属职场']
# df_second['序号'] = range(1, len(df_second)+1)  # 写入序号
print('完成处理：<转介绍表>')

# 处理第三张多重奖励名单
# print('开始处理:<多重奖励名单>...')
df_second_get_card = df_second[df_second['卡激活日期'].notnull()].reset_index(drop=True)  # 筛选出转介绍客户已开卡数据
count = df_second_get_card['一级客户手机号'].value_counts()  # 统计一级客户邀请数量
dict_count = {'手机号': count.index, '开卡数量': count.values}  # series转换为dict
df_count = pd.DataFrame(dict_count)  # 用此dict格式创建df
df_second_get_card = df_second_get_card.drop_duplicates(subset='一级客户手机号')  # 多重奖励一级客户去重
df_get_card_count = pd.merge(df_second_get_card, df_count, how='left', left_on='一级客户手机号', right_on="手机号")
df_get_card_count['开卡数量'] = df_get_card_count['开卡数量'].fillna(0)
df_get_card_count['开卡数量'] = df_get_card_count['开卡数量'].astype('int64')
# print(df_get_card_count)

df_third['客户姓名'] = df_get_card_count['一级客户姓名']
df_third["客户手机号"] = df_get_card_count['一级客户手机号']
df_third["绑定营销员"] = df_get_card_count['绑定营销员']
df_third["绑定营销员工号"] = df_get_card_count['绑定营销员工号']
df_third["所属机构"] = df_get_card_count['所属机构']
df_third["所属职场"] = df_get_card_count['所属职场']
df_third["邀请激活人数"] = df_get_card_count['开卡数量']
#df_third["具备送蔬菜资格"] = '否'
#df_third["具备白金卡升级资格"] = '否'

# 下面操作会产生SettingWithCopyWarning
# 隐藏warning信息
pd.options.mode.chained_assignment = None  # default='warn'
# df_third['具备送蔬菜资格'][df_third['邀请激活人数'] >= 3] = '是'
# df_third['具备白金卡升级资格'][df_third['邀请激活人数'] >= 3] = '是'

df_third = df_third[df_third['客户姓名'].notnull()].reset_index(drop=True)  # 筛选出客户姓名非空的行
# df_third['序号'] = range(1, len(df_third)+1)
print('完成处理：<多重奖励名单>')

# 卡激活信息表
# print('开始处理<卡激活表>')
df_card_info = pd.merge(df_card, df_info, how='left', left_on='营销员工号', right_on='客户经理工号')
df_card_info = df_card_info.drop_duplicates(subset='卡激活日期', keep='first')  # 未知原因导致匹配后存在重复数据
df_card_info = df_card_info.reset_index(drop=True)  # 重置索引
df_card['机构'] = df_card_info['二级名称']
print('完成处理：<卡激活表>')

# 无效报名表
# print('开始处理<无效报名表>')
df_invalid_detail = df_first[df_first['绑定营销员'].isnull()]
df_invalid_detail_info = pd.merge(df_invalid_detail, df_card, how='left', left_on='客户手机号', right_on="用户手机号")
df_invalid['报名日期'] = df_invalid_detail_info['报名日期']
df_invalid['客户姓名'] = df_invalid_detail_info['客户姓名']
df_invalid['客户手机号'] = df_invalid_detail_info['客户手机号']
df_invalid['卡产品名称'] = df_invalid_detail_info['卡产品名称_y']
df_invalid['卡激活日期'] = df_invalid_detail_info['卡激活日期_y']
df_invalid['绑定营销员'] = df_invalid_detail_info['营销员姓名']
df_invalid['绑定营销员工号'] = df_invalid_detail_info['营销员工号']
df_invalid['所属机构'] = df_invalid_detail_info['机构']
print('完成处理：<无效报名表>')

# 代人激活表
df_cheat_card_info = pd.merge(df_cheat_card, df_info, how='left', left_on='营销员工号', right_on='客户经理工号')
df_cheat_card['机构'] = df_cheat_card_info['二级名称']

# 获取分公司列表
company_count = df_first['所属机构'].value_counts()

t3 = time.time()
print('处理完成,耗时%.2fs' % (t3-t2))

print('开始写入...')
"""
for company in company_count.index:
    writer = pd.ExcelWriter(PATH + '..//内蒙古%s活动日报数据'%company + TIME + '.xlsx')
    # 按公司分别筛选表
    df_first_company = df_first[df_first['所属机构'] == company]
    df_second_company = df_second[df_second['所属机构'] == company]
    df_third_company = df_third[df_third['所属机构'] == company]
    df_card_company = df_card[df_card['机构'] == company]
    df_cheat_card_company = df_cheat_card[df_cheat_card['机构'] == company]
    df_invalid_company = df_invalid[df_invalid['所属机构'] == company]
    # 分别写入
    df_first_company.to_excel(writer, sheet_name='报名表', index=False)
    df_second_company.to_excel(writer, sheet_name='转介绍表', index=False)
    df_third_company.to_excel(writer, sheet_name='多重奖励名单', index=False)
    df_card_company.to_excel(writer, sheet_name='卡激活信息', index=False)
    df_invalid_company.to_excel(writer, sheet_name='无效报名', index=False)
    df_cheat_card_company.to_excel(writer, sheet_name='代人激活表', index=False)
    writer.save()
    print('%s报表写入完成'%company)
"""

writer = pd.ExcelWriter(PATH + '..//天津汇总活动日报数据' + TIME + '.xlsx')
df_first.to_excel(writer, sheet_name='报名表', index=False)
df_second.to_excel(writer, sheet_name='转介绍表', index=False)
df_third.to_excel(writer, sheet_name='多重奖励名单', index=False)
df_card.to_excel(writer, sheet_name='卡激活信息', index=False)
df_invalid.to_excel(writer, sheet_name='无效报名', index=False)
# df_cheat_card.to_excel(writer, sheet_name="代人激活表", index=False)
writer.save()

t4 = time.time()
print('写入完成，耗时%.2fs' % (t4-t3))
print('今日报表已完成\n共耗时：%.2fs' % (t4-t1))
