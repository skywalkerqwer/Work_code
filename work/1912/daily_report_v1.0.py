"""
    生成陈静的每日汇报内容
    需要先完成今日汇总报表
"""

import pandas as pd
import time

# 输出语句
s1 = "各位领导好，最新健康管家献礼活动数据汇报如下：\n"
s2 = "1、内蒙参与活动营销员%d位，已经完成绑定的共计%d位，绑定率%.2f%%\n"
s3 = "2、参与海报活动裂变的营销员%d位；参与率%.2f%%；\n"
s4 = "3、海报成功裂变中：1级客户%d位，%d位开通健康管家金卡；一级客户开卡率为%.2f%%，\n"
s5 = "4、1级客户海报成功裂变2级客户中：%d位一级客户带来%d位客户，其中：%d位客户二级开通健康管家金卡；\n"
s6 = "5、报名活动并开通健康管家金卡的客户共%d位。\n"
s7 = "【数据起止：12月10日至 %s 17:00】"

# 常参
TIME = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 当日日期  2019-12-06
START_TIME = '2019-12-10 00:00:00'  # 活动开始时间
PATH = r'C:\Users\Healthlink\Desktop\日报统计数据\内蒙国寿\数据源\\'
FILE_DATA = r'..\内蒙古汇总活动日报数据' + TIME + '.xlsx'  # 汇总数据
FILE_SALE = r'员工列表.csv'  # 员工列表

df_data_first = pd.read_excel(PATH + FILE_DATA)
df_data_second = pd.read_excel(PATH + FILE_DATA, sheet_name='转介绍表')
df_sale = pd.read_csv(PATH + FILE_SALE, engine='python')

# s2内容
df_sale_num = df_sale[df_sale['手机号'].notnull()]  # 备案员工表
sale_num = len(df_sale_num)  # 员工备案量
df_sale_binding = df_sale[df_sale['绑定状态'] == "已绑定"]  # 绑定员工表
binding_sale_num = len(df_sale_binding)  # 绑定员工量
binding_rate = (binding_sale_num/sale_num)*100  # 绑定率

# s3内容
se_join_sale = df_data_first['绑定营销员'].value_counts()
join_sale_num = len(se_join_sale)  # 参与活动的营销员
join_rate = (join_sale_num/sale_num)*100  # 参与率

# s4内容
first_member_num = len(df_data_first)  # 报名人数
first_member_card_num = len(df_data_first[df_data_first['卡产品名称'].notnull()])  # 一级开卡数量
active_card_rate = (first_member_card_num/first_member_num)*100  # 开卡率

# s5内容
second_first_num = len(df_data_second['一级客户手机号'].value_counts())  # 带来二级客户的一级客户数量
second_member_num = len(df_data_second)  # 转介绍客户数
second_member_card_num = len(df_data_second[df_data_second['卡产品名称'].notnull()])  # 二级开卡数量

# s6内容
total_active_card_num = first_member_card_num + second_member_card_num

s2 = s2 % (sale_num, binding_sale_num, binding_rate)
s3 = s3 % (join_sale_num, join_rate)
s4 = s4 % (first_member_num, first_member_card_num, active_card_rate)
s5 = s5 % (second_first_num, second_member_num, second_member_card_num)
s6 = s6 % (total_active_card_num)
s7 = s7 % (TIME)

print(s1 + s2 + s3 + s4 + s5 + s6 + s7)
