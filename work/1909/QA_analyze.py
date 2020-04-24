"""
将字段拆分
获取真实答题数量
获取跳出问题
"""
import pandas as pd
import numpy as np
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 防止乱码

PATH = r'D:\数据\慢病QA数据\提取\\'
FILE = '慢病用户问答数据2019-10-14.xlsx'

origin = pd.read_excel(PATH + FILE)  # 原始数据
# print(origin)
# print(origin.columns)

answer = origin[['问题'+str(i)+'答案' for i in range(1, 51)]]
# print(answer)
answer = answer.fillna('N/A')

answer_n = (answer != 'N/A').sum(axis=1)  # 统计真实回答问题数量
counts = pd.value_counts(answer_n)
# print(counts)


# 获取每行最后一个非空元素，若全空则返回空
def get_last(x):
    if x.last_valid_index() is None:
        return np.nan
    else:
        return x[x.last_valid_index()]


questions = origin[['问题'+str(i) for i in range(1, 51)]]
# print(questions)
questions_re = questions.apply(get_last, axis=1)
questions_re = questions_re.dropna(axis=0)
# print(questions_re)

count_questions = questions_re.value_counts()
# print(count_questions)

# out_time = pd.DataFrame()
# out_time['姓名'] = origin['姓名']
# out_time['身份证号'] = origin['身份证号']
# out_time = pd.concat(out_time,origin[['问题'+str(i)+'答案时间' for i in range(1, 51)]])
# print(out_time)

with open('D:\Code\work\data\id_area.txt', 'r', encoding='UTF-8') as f:
    area = eval(f.read())  # 省份经纬度 --> "北京市":"39.55,116.24"

gender = {
    0: '女',
    1: '男'
}

def get_area(x):
    code = x[:2]
    code = code + '0000'
    return area[code]


def get_gender(x):
    x = int(x[-2])
    x = x % 2
    return gender[x]


def get_age(x):
    age = 2019 - int(x[6:10])
    return age


def divide_age(x):
    d = {
        2: '0-5',
        7: '5-10',
        12: '10-15',
        17: '15-20',
        22: '20-25',
        27: '25-30',
        32: '30-35',
        37: '35-40',
        42: '40-45',
        47: '45-50',
        52: '50-55',
        57: '55-60',
        62: '60-65',
        67: '65-70',
        72: '70-75',
        77: '75-80',
        82: '80-85',
        87: '85-90',
        92: '90-95',
        97: '95-100',
        102: '100-105',
    }
    i = x//5
    i = i*5 + 2
    try:
        s = d[i]
    except:
        s = '异常'
    return s


df_new = pd.DataFrame()
df_new['地区'] = origin['身份证号'].apply(get_area)
df_new['性别'] = origin['身份证号'].apply(get_gender)
df_new['年龄'] = origin['身份证号'].apply(get_age)
df_new["年龄分段"] = df_new['年龄'].apply(divide_age)

writer = pd.ExcelWriter('统计_' + FILE)
# count_questions.to_excel(writer, '跳出问题统计', index = True)
# counts.to_excel(writer, '答题数量统计', index=True)
df_new.to_excel(writer)
writer.save()
