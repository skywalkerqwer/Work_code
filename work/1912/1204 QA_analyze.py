"""
肖蓥提出分析需求
"""

import pandas as pd
import numpy as np
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 防止乱码

PATH = r'D:\数据\慢病QA数据\提取\\'
FILE = '慢病用户问答数据2019-12-16.xlsx'

df_origin = pd.read_excel(PATH + FILE)  # 原始数据

with open(r'D:\Code\work\data\area.txt', 'r', encoding='UTF-8') as f:
    area = eval(f.read())


gender = {
    0: '女',
    1: '男'
}


def get_first_area(x):
    code = x[:2]
    code = code + '0000'
    return area[code]


def get_second_area(x):
    code = x[:4]
    code = code + '00'
    try:
        re = area[code]
        return re
    except KeyError:
        return '匹配错误'


def get_gender(x):
    x = int(x[-2])
    x = x % 2
    return gender[x]


def get_age(x):
    age = 2019 - int(x[6:10])
    return age


# 获取每行最后一个非空元素，若全空则返回空
def get_last(x):
    if x.last_valid_index() is None:
        return np.nan
    else:
        return x[x.last_valid_index()]


df_last_ques = df_origin[['问题'+str(i) for i in range(1, 51)]]
questions_re = df_last_ques.apply(get_last, axis=1)
questions_re = questions_re.dropna(axis=0)

valid_ans_df = df_origin.dropna(axis=0, subset=['问题1'])
answer_time = valid_ans_df[['问题'+str(i)+'答案时间' for i in range(1, 51)]]
answer_time = answer_time.astype('datetime64')


df = pd.DataFrame()
df['姓名'] = df_origin['姓名']
df['身份证号'] = df_origin['身份证号']
df['性别'] = df_origin['身份证号'].apply(get_gender)
df['年龄'] = df_origin['身份证号'].apply(get_age)
df['一级地区'] = df_origin['身份证号'].apply(get_first_area)
df['二级地区'] = df_origin['身份证号'].apply(get_second_area)
df['答题数量'] = df_origin['回复问题个数']
df['最早答题时间'] = answer_time.min(axis=1)
df['最后答题时间'] = answer_time.max(axis=1)
df['答题间隔天数'] = df['最后答题时间'] - df['最早答题时间']


writer = pd.ExcelWriter(PATH + '../1216 QA用户分析.xlsx')
df.to_excel(writer, sheet_name='基本画像', index=False)
questions_re.to_excel(writer, sheet_name='跳出问题', index=False)
writer.save()
