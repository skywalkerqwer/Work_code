"""
    更新话术版本
"""

import pandas as pd
import time,datetime

# 输出语句
head = "各位领导好，最新健康管家活动数据汇报如下：\n"
s1 = "1、营销员共备案%d人，完成领取海报共%d人，海报参与率为%.2f%%。"
s2 = "2、%d位营销员的海报被%d位客户扫描了%d次，平均每位营销员的海报被扫描%d次，共%d位一级客户报名成功，报名率为%.2f%%，平均每有%.1f人扫码将带来一位有效报名客户。"
s3 = "3、%d位营销员共带来%d位一级有效客户，其中有%d位客户成功开通了健康管家金卡，开卡率为%.2f%%。"
s4 = "4、平均每位营销员带来%d位客户，帮助客户开通%d张金卡。"
s5 = "5、在%d位报名的一级客户中有%d位生成了自己的会员海报，海报生成率为%.2f%%。"
s6 = "6、由%d位一级客户带来了%d位二级客户，平均每位一级客户带来%.1f位转介绍客户，转介绍率为%.2f%%。"
s7 = "7、%d位二级客户中，有%d位客户成功开通健康管家金卡，开卡率为%.2f%%。"
s8 = "8、%d位领取海报的一级客户中，有%d位具备奖励资格，完成率为%.2f%%。"
s9 = "9、本次活动目前共激活%d张健康管家金卡。"
s10 = '10、今日备案营销员%d位，今日开卡%d张。'
tail = "【数据起止：12月10日至 %s 17:00】"

# 常参
# TIME = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 当日日期  2019-12-06
TIME = datetime.date.today()
yesterday = TIME - datetime.timedelta(days=1)
TIME = str(TIME)
yesterday = str(yesterday)
yesterday_h = yesterday + ' 17:00'  # 从昨日17点开始记录
START_TIME = '2019-12-10 00:00:00'  # 活动开始时间
PATH = r'C:\Users\Healthlink\Desktop\日报统计数据\内蒙国寿\数据源\\'
FILE_DATA = r'..\内蒙古汇总活动日报数据' + TIME + '.xlsx'  # 汇总数据
FILE_SALE = r'员工列表.csv'  # 员工列表
FILE_SALE_INVITE = r'【邀请明细】国寿臻心七十载庆典钜献福临门营销员海报' + TIME + '.csv'
FILE_SALE_PARTY = r'【参与统计】国寿臻心七十载庆典钜献福临门营销员海报' + TIME + '.csv'
FILE_MEMBER_INVITE = r'【邀请明细】国寿臻心七十载庆典钜献福临门会员海报' + TIME + '.csv'
FILE_MEMBER_PARTY = r'【参与统计】国寿臻心七十载庆典钜献福临门会员海报' + TIME + '.csv'

# 读取文件
df_data_first = pd.read_excel(PATH + FILE_DATA)
df_data_second = pd.read_excel(PATH + FILE_DATA, sheet_name='转介绍表')
df_data_third = pd.read_excel(PATH + FILE_DATA, sheet_name='多重奖励名单')
df_sale = pd.read_csv(PATH + FILE_SALE, engine='python')
df_sale_invite = pd.read_csv(PATH + FILE_SALE_INVITE, engine='python')
df_sale_party = pd.read_csv(PATH + FILE_SALE_PARTY, engine="python")
df_member_invite = pd.read_csv(PATH + FILE_MEMBER_INVITE, engine='python')
df_member_party = pd.read_csv(PATH + FILE_MEMBER_PARTY, engine='python')

# s1内容
df_sale_num = df_sale[df_sale['手机号'].notnull()]  # 备案员工表
sale_register_num = len(df_sale_num)  # 员工备案量
sale_poster_num = len(df_sale_party)  # 领取海报员工数
poster_register = (sale_poster_num/sale_register_num) * 100  # 员工海报参与率

# s2内容
df_sale_invite_scan = df_sale_invite[df_sale_invite['行为内容'] == '扫码二维码']
poster_scan_member = len(df_sale_invite_scan['被邀请人openid'].value_counts())  # 扫描员工海报二维码的人数
poster_scan_num = len(df_sale_invite_scan)  # 扫描员工海报二维码的次数
avg_scan_num = poster_scan_num / sale_poster_num  # 平均海报扫描次数
poster_enter_num = len(df_sale_invite[df_sale_invite['行为内容'] == '会议报名'])  # 会议报名人数
enter_rate = (poster_enter_num / poster_scan_member) * 100  # 报名率
avg_scan_enter = poster_scan_member / poster_enter_num  # 平均带来一个客户的扫描人数

# s3内容
first_member_num = len(df_data_first)  # 一级报名人数
first_member_card_num = len(df_data_first[df_data_first['卡产品名称'].notnull()])  # 一级开卡数量
first_active_card_rate = (first_member_card_num/first_member_num) * 100  # 开卡率

# s4内容
join_sale_num = len(df_data_first['绑定营销员'].value_counts())  # 参与活动的营销员
avg_sale_invite_num = first_member_num / join_sale_num  # 平均每位营销员带来客户量
avg_sale_active_card = first_member_card_num / join_sale_num  # 平均每位营销员帮助客户开卡量

# s5内容
member_poster_num = len(df_member_party)  # 生成会员海报的一级客户量
creat_poster_rate = (member_poster_num / first_member_num) * 100  # 海报生成率

# s6内容
second_first_num = len(df_data_second['一级客户手机号'].value_counts())  # 带来二级客户的一级客户数量
second_member_num = len(df_data_second)  # 转介绍客户数
avg_first_invite_num = second_member_num / second_first_num  # 平均每位一级客户带来的转介绍客户量
first_invite_rate = (second_member_num / first_member_num) * 100  # 转介绍率

# s7内容
second_member_card_num = len(df_data_second[df_data_second['卡产品名称'].notnull()])  # 二级开卡数量
second_active_card_rate = (second_member_card_num / second_member_num) * 100  # 二级客户开卡率

# s8内容
award_num = len(df_data_third[df_data_third['具备白金卡升级资格'] == '是'])  # 具备奖励资格人数
achieve_rate = (award_num / member_poster_num) * 100  # 完成率

# s9内容
total_active_card_num = first_member_card_num + second_member_card_num

# s10内容
new_sale_num = len(df_sale[df_sale['注册时间'] >= yesterday])  # 今日注册营销员数量
new_fist_active_card_num = len(df_data_first[df_data_first['卡激活日期'] >= yesterday_h])  # 今日一级开卡数量
new_second_active_card_num = len(df_data_second[df_data_second['卡激活日期'] >= yesterday_h])  # 今日二级开卡数量
new_total_active_card_num = new_fist_active_card_num + new_second_active_card_num  # 今日总开卡量

# 补齐数值
s1 = s1 % (sale_register_num, sale_poster_num, poster_register)
s2 = s2 % (sale_poster_num, poster_scan_member, poster_scan_num, avg_scan_num, poster_enter_num, enter_rate, avg_scan_enter)
s3 = s3 % (sale_poster_num, first_member_num, first_member_card_num, first_active_card_rate)
s4 = s4 % (avg_sale_invite_num, avg_sale_active_card)
s5 = s5 % (first_member_num, member_poster_num, creat_poster_rate)
s6 = s6 % (second_first_num, second_member_num, avg_first_invite_num, first_invite_rate)
s7 = s7 % (second_member_num, second_member_card_num, second_active_card_rate)
s8 = s8 % (member_poster_num, award_num, achieve_rate)
s9 = s9 % (total_active_card_num)
s10 = s10 % (new_sale_num, new_total_active_card_num)
tail = tail % TIME

result = ''

for i in range(1, 11):
    result += eval('s' + str(i)) + '\n'

print(head + result + tail)
