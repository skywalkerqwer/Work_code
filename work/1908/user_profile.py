"""
用户画像
"""
import pandas as pd
import numpy as np
from datetime import datetime

user = pd.read_excel(r'C:\Users\Healthlink\Desktop\数据\天津国寿电话医生数据\用户按活跃分类.xls', sheet_name='不满足月活用户')
user = user[['姓名', '年龄', '性别', '电话', '二级专业分类', '客户主诉', '印象/诊断', '服务时间']]

all_user = pd.read_excel(r'C:\Users\Healthlink\Desktop\数据\中医检测活动数据\天津卡激活数据提取.xls')

# 处理年龄空值和数据类型
user['年龄'] = user['年龄'].fillna(-1)
user['年龄'] = user['年龄'].apply(lambda x:int(x))
# print(df[df['年龄'] == -1])

"""
print(df['服务时间'])
669   2019-08-11 12:29:00
670   2019-08-12 10:56:10
Name: 服务时间, Length: 671, dtype: datetime64[ns]
"""

all_user['卡激活日期'] = all_user['卡激活日期'].apply(lambda x:int(x[5: 7]))
all_user = all_user.drop_duplicates(subset='用户手机号', keep='first')
# print(all_user.head(3))
"""
      机构    营销员工号 营销员姓名  卡激活日期  ...  用户名 用户性别  用户年龄    用户手机号
0     NaN  1.202358e+13   周郑州      8        ...  李庆华    女      42    18202298805
1     NaN  1.202358e+13   马晓云      8        ...   邢珺     女     53    13920518007
"""

# 得到用户来电月份
user['服务时间'] = user['服务时间'].map(str)
user['month'] = user['服务时间'].apply(lambda x: x[5:7]).astype('int')
# print(df)
# print('*' * 50)
used_user = user.sort_values(by='姓名')

# print(df_user)
unfinde_user = pd.DataFrame()
active_user = pd.DataFrame()
for phone, group in used_user.groupby('电话'):
    # 按来电月份排序
    group = group.sort_values(by='month')
    # 去重
    group = group.drop_duplicates(subset='month')
    # 获取最早开卡月份
    try:
        early_month = all_user[all_user['用户手机号'] == phone]['卡激活日期'].values[0]
    except IndexError:
        # 手机号匹配无效的用户
        print('*'*30)
        temp = used_user[used_user['电话'] == phone]
        print(temp)
        unfinde_user = unfinde_user.append(temp)
        continue
    # print(group)

    if len(group.index) == 9 - early_month:  # 开卡之后每个月都打电话的用户定义为活跃用户
        print('-'*30)
        print(group)
        active_user = active_user.append(group)


print('='*50)
print("无信息用户：")
print(unfinde_user)

print('='*50)
print('活跃用户')
print(active_user)

writer = pd.ExcelWriter('活跃用户与未匹配用户.xls')
active_user.to_excel(writer, '活跃用户', index = False)
unfinde_user.to_excel(writer, '未匹配用户', index = False)
writer.save()
