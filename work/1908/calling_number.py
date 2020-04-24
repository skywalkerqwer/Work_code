# -*- coding=utf-8 -*-
# coding=utf-8
"""
绘制每天 每小时来电量
"""

import tools_excel as tool
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dfs = tool.get_all_sheet(r'C:\Users\Healthlink\Desktop\数据\电话3-8.xlsx')

df = dfs[0]
df = df.reindex(columns=['来电编号'])

# print(df)
"""
    来电编码  day_call  hour_call
0   2019801092805230       NaN        NaN
1   2019801102205890       NaN        NaN
2   2019801102906010       NaN        NaN
"""


def cal_time(t):
    """
    t : 2019801092805230
        2019 - 8 - 01  09 : 2 8 :05.230
        0123 - 4 - 56  78: 9 10 :11
    """
    t = str(t)
    year = t[:4]
    month = t[4]
    day = t[5:7]
    hour = t[7:9]
    return "{}-{}-{} {}".format(year, month, day, hour)


def day_call(t):
    t = str(t)
    day = t[7:9]
    return int(day)


def hour_call(t):
    t = str(t)
    hour = t[10:]
    return int(hour)


def month(t):
    t = str(t)
    month = t[5]
    return int(month)


def year(t):
    t = str(t)
    year = t[:4]
    return int(year)

def data(t):
    t = str(t)
    data = t[:9]
    return data

df['来电编号'] = df['来电编号'].transform(cal_time)
df['day'] = df['来电编号'].transform(day_call)
df['hour'] = df['来电编号'].transform(hour_call)
df['month'] = df['来电编号'].transform(month)
df['year'] = df['来电编号'].transform(year)
df['data'] = df['来电编号'].transform(data)

df = df.sort_values(by=['来电编号'], ascending=True)
print(df)
# print(df[df['month']==1])

dfs_by_month = []
for i in range(1, 13):
    df_new = df[df['month'] == i]
    dfs_by_month.append(df_new)

# print(df[df['month']==1])

# print(df[['day_call', 'hour_call']])
# df_by_month = pd.DataFrame(df[['day', 'hour']], index=df['month'])
# print(df_by_month)
"""
             来电编号  day_call  hour_call  month
0    2019-3-01 11         1         11      3
1    2019-3-01 11         1         11      3
2    2019-3-04 09         4          9      3
"""
# day_num = pd.value_counts(df['day_call'])
# day_num = pd.value_counts(df_by_month['day_call'])
# print(day_num)
"""
1     6
6     4
3     4
9     3
"""
# day_num.sort_index(inplace=True)  # 按索引排序
# day_num = day_num.reindex(np.arange(1,32), fill_value=0)  # 扩充索引
# print(day_num)
"""
1     6.0
2     3.0
3     4.0
4     2.0
"""

"""
# 绘制子图 按月统计每天来电量
plt.figure('Each day calling in month')

for i,d in enumerate(dfs_by_month):
    d = pd.value_counts(d['day'])
    d.sort_index(inplace=True)  # 按索引排序
    d = d.reindex(np.arange(1,32), fill_value=0)  # 扩充索引
    plt.subplot(4,3,i+1)
    plt.title('month {}'.format(i+1))
    d.plot(style='--', linewidth=1)
    # plt.tick_params(labelsize=8)
    # plt.gcf().autofmt_xdate()
    # plt.xticks(np.arange(1, 32))
    plt.tight_layout()
    plt.autoscale()

plt.savefig('month_calling', bbox_inches='tight', dpi=1200)
plt.show()
"""

"""
# 绘制每月统计 在一张折线图
plt.figure('Each day calling in month')
for i, d in enumerate(dfs_by_month):
    d = pd.value_counts(d['day'])
    d.sort_index(inplace=True)  # 按索引排序
    d = d.reindex(np.arange(1, 32), fill_value=0)  # 扩充索引
    plt.title('Each month calling')
    d.plot(style='--', linewidth=1, label='{}'.format(i + 1))
    # plt.tick_params(labelsize=8)
    # plt.gcf().autofmt_xdate()
    # plt.xticks(np.arange(1, 32))
    plt.tight_layout()
    plt.autoscale()
    plt.legend()

plt.savefig('month_calling', bbox_inches='tight', dpi=1200)
plt.show()
"""

"""
plt.figure('day/hour calling plot')

plt.subplot(211)
plt.title('Day Calling Num')
day_num.plot(style='o--')
plt.xticks(np.arange(1,32))
plt.autoscale()

plt.subplot(212)
plt.title('Hour Calling Num')
hour_num.plot(style='o--')
plt.xticks(np.arange(1,25))
plt.autoscale()

plt.show()
"""

"""
# 总计每小时来电量
hour_num = pd.value_counts(df['hour'])
hour_num = hour_num.reindex(np.arange(1,25), fill_value=0)
# print(hour_num)
plt.figure('Hour calling plot')
plt.title('Hour Calling Num')
hour_num.plot(style='--')
plt.xticks(np.arange(1,25))
plt.autoscale()

plt.show()
"""

"""
绘制连续3-8月来电量图
"""
data_df = pd.value_counts(df['data'])
data_df.sort_index(inplace=True)
print(data_df)
data_df.plot(linewidth=1)
plt.show()
