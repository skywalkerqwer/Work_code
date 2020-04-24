import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(r'C:\Users\Healthlink\Desktop\健康咨询.xlsx')

df = df[['年龄', '性别']].fillna('')

df = df.drop(df[df['年龄'] == '' ].index)  # 去掉脏数据
df = df.drop(df[df['性别'] == ''].index)

df['年龄'] = df['年龄'].astype('str')

def reg_age(x):
    if '月' in x or '天' in x:  # 去掉 6个月 20天
        x = '1'
        return x
    if x[-1] == '半':  # 2周岁半  --> 2周岁
        x = x[:-1]
    if x[-1] == '周':  # 10周 --> 1
        x = '1'
        return x
    if x[-1] == '岁':  # 50周岁 50多岁  --> 50周 50多
        x = x[:-1]
        if x[-1] == '周' or x[-1] == '多':  # 50周 50多 --> 50
            x = x[:-1]
    if x[-1] == '多':  # 去掉 50多
        x = x[:-1]
    if '岁' in x:  # 保险
        x = x[:2]
    return x


def round_age(x):
    # 年龄四舍五入
    head = x // 10
    temp = (x % 10) // 5
    x = (head + temp) * 10
    return x


df['年龄'] = df['年龄'].transform(reg_age)
df['年龄'] = df['年龄'].astype('float')
df['年龄'] = df['年龄'].transform(round_age)

gender = pd.DataFrame(data=None, index=range(0,90,10), columns=['male', 'female'])

for i in range(9):
    # 0 - 80岁
    age = 10 * i
    new_df = df[df['年龄'] == age]
    male = new_df[new_df['性别'] == '男']['性别'].count()
    female = new_df[new_df['性别'] == '女']['性别'].count()
    gender.loc[age, 'male'] = male
    gender.loc[age, 'female'] = female
print(gender)
# plt.figure('Age of gender')
plt.title('Age of gender')
gender.plot.bar()

plt.show()
