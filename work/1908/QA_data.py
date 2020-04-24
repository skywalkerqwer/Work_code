"""
分析慢病用户问答数据
用户画像
"""
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 防止乱码
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('D:\Code\work\data\id_are.txt', 'r', encoding='UTF-8') as f:
    area = eval(f.read())  # 身份证归属地字典 --> {"110000" : "北京市"}

gender = {
    0: '女',
    1: '男'
}

df = pd.read_excel(r'C:\Users\Healthlink\Desktop\20190822慢病用户问答数据统计.xlsx', sheet_name='有答题')


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


def round_age(x):
    # 年龄四舍五入
    head = x // 10
    temp = (x % 10) // 5
    x = (head + temp) * 10
    return x

df_new = pd.DataFrame()
df_new['A_num'] = df['回复问题个数']
df_new['area'] = df['身份证号'].apply(get_area)
df_new['gender'] = df['身份证号'].apply(get_gender)
df_new['age'] = df['身份证号'].apply(get_age)
df_new['age'] = df_new['age'].apply(round_age)
# print(df_new)
"""
    A_num area gender  age
0      58  北京市      男   46
1      56  四川省      女   31
2      42  吉林省      男   31
3      30  四川省      男   27
4      30  四川省      女   22
"""
# 中位数为13 筛选忠实用户
# df_new = df_new[df_new['A_num'] >= 13]

"""
# 地区统计分类
# count = pd.value_counts(df_new[df_new['A_num'] >= 13]['area'])
count = pd.value_counts(df_new['area'])
print(count)
count.plot.bar()
"""

"""
# 性别年龄统计
gender_df = pd.DataFrame(data=None, index=range(0,90,10), columns=['male', 'female'])
for i in range(9):
    # 0 - 80岁
    age = 10 * i
    count_df = df_new[df_new['age'] == age]
    male = count_df[count_df['gender'] == '男']['gender'].count()
    female = count_df[count_df['gender'] == '女']['gender'].count()
    gender_df.loc[age, 'male'] = male
    gender_df.loc[age, 'female'] = female
gender_df.plot.bar()
plt.show()
"""

# 进行忠实与非忠实分类并画图
"""
df_new['class'] = df_new['A_num'].apply(lambda x:'忠实用户' if x >=13 else '非忠实用户')

count = df_new[df_new['class'] == '忠实用户']
count = pd.value_counts(count['gender'])
count.plot.pie()

# df_male = df_new[df_new['gender']=='男']
# df_female = df_new[df_new['gender']=='女']

# print(pd.value_counts(df_new['gender']))  # female : male  =  57 : 37
# count_male = pd.value_counts(df_male['class'])  # 23/14 = 62%
# count_female = pd.value_counts(df_female['class'])  # 24/33 = 42%

# print(count_female)
# count_female.plot.pie()
plt.show()
"""

"""
# 统计高频跳出问题（目前数据只能看到跳出的前一个问题）
# 305:307 -->  问题1  问题1答案
q_a = df.iloc[:,305:-1]
q_a = q_a.dropna(axis=1, how='all')  # 问题1 -- 问题58
# 掩码获取所有问题列
b = np.arange(104)
mask = b % 2 == 0
questions = q_a.iloc[:, mask]

questions.to_excel('all_questions.xls')
"""

# last = pd.read_excel(r'C:\Users\Healthlink\Desktop\last_questions.xlsx')
# count = pd.value_counts(last['跳出问题'])
# print(count)
"""
all = pd.read_excel(r'C:\Users\Healthlink\Desktop\all_questions.xlsx')
count = pd.value_counts(all['问题'])
print(count.head(10))
# plt.title('跳出问题')
# plt.title('提问问题')
count.plot.bar()
plt.xticks([])
plt.autoscale()
plt.show()
"""

"""
# 统计答题数量
count = pd.value_counts(df_new['A_num'])
plt.title('答题数量')
count.plot.bar()
plt.show()
"""
