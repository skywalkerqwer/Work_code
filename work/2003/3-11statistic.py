"""
统计服务元素
"""
import pandas as pd

df = pd.read_excel(r'D:\数据\基因微磁数据客户.xlsx')


df_concat= pd.DataFrame()
for i in range(1, 51):
    df_concat = pd.concat([df_concat, df['元素'+str(i)]], ignore_index=True)


count = df_concat.iloc[:, 0].value_counts()  # 取第一列
dict_count = {'服务元素':count.index, '出现频数':count.values}
df_count = pd.DataFrame(dict_count)

writer = pd.ExcelWriter('服务元素统计.xlsx')
df_count.to_excel(writer, index=False)
writer.save()
