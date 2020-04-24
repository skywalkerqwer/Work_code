# -*- coding=utf-8 -*-
# coding=utf-8

import tools_excel as tool
import pandas as pd
import matplotlib.pyplot as plt

dfs = tool.get_all_sheet(r'C:\Users\Healthlink\Desktop\数据\健康咨询.xlsx')

df = dfs[0]

female = (df['性别'] == '女').sum()
male = (df['性别'] == '男').sum()
total = len(df.index)

# labels = ['male', 'female', 'null']  # 有未标性别的
labels = ['male', 'female']
# size = [male, female, total-male-female]
size = [male, female]
# spaces = [0.1, 0.1, 0.1]
spaces = [0.1, 0.1]

plt.figure('Gender per')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 防止中文乱码出现
plt.pie(size, spaces,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90)
plt.title('Gender per')
plt.axis('equal')
plt.savefig('Gender.png', dpi=300)
plt.show()
