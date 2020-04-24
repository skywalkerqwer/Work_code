# -*- coding: UTF-8 -*-
"""
    以2019-12月内蒙国寿活动为模板，生成每日报表
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
START_TIME = '2019-12-10 00:00:00'  # 活动开始时间
PATH = r'C:\Users\Healthlink\Desktop\日报统计数据\内蒙国寿\数据源\\'
print('今天日期为：', TIME)


def replace_c(x):
    x = str(x)
    x = x.replace(',', '')
    x = x.replace('，', '')
    return x


# 文件名称
FILE_sales_info = r'员工列表.csv'

# 读取两个会议数据和营销员备案数据

df_info = pd.read_csv(PATH + FILE_sales_info, engine='python')  # 营销员备案
# 处理员工列表信息
df_info['客户经理工号'] = df_info['客户经理工号'].fillna(0)
df_info['客户经理工号'] = df_info['客户经理工号'].apply(replace_c)
df_info['客户经理工号'] = df_info['客户经理工号'].astype('int64')
print(df_info)