# -*- coding=utf-8 -*-
# coding=utf-8

import tools_excel as tool
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfs = tool.get_all_sheet(r'C:\Users\Healthlink\Desktop\数据\tjgs_calllist.xlsx')

df = dfs[0]

# 获取索引列表
df_new = df.drop_duplicates(subset='年龄',keep='first',inplace=False)
df_new = df_new.iloc[:,1:-9].fillna('null')
df_new = df_new[df_new['年龄'] != 'null']
new_index = df_new['年龄'].tolist()
# print(new_index)


df = df.iloc[:,1:-9].fillna('null')  # 切片填null
df = df.drop(['医生工号', '科室组别', '会员姓名', '电话'], axis=1)  # 去掉无用特征
df = df[df['年龄'] != 'null']  # 去掉年龄为空的用户

# print('df1--------------')
# print(df)
"""
             产品名称  年龄    性别 专业分类一
1     天津国寿健康管家白金卡  24     男    外科
2      天津国寿健康管家金卡  25     女   妇产科
3      天津国寿健康管家金卡  76     男    内科
"""
df2 = pd.DataFrame(np.zeros(len(new_index), None),index=new_index, dtype='int32')
# print(df2)


card = pd.value_counts(df['产品名称'])
print(card)
sex = pd.value_counts(df['性别'])
print(sex)
look = pd.value_counts(df['专业分类一'])
print(look)


# df.plot.bar()
# plt.show()