"""
挑选出包含医疗咨询和健康档案的用户的电话医生记录
"""
import pandas as pd

df_user = pd.read_excel(r'D:\Code\work\2003\筛选服务元素-健康档案.xlsx')
df_all = pd.read_excel(r'D:\数据\电话医生\健康咨询结构化数据.xlsx')
# df_user['电话'].astype('str')
#
# for i in df_user['电话']:
#     df_out = pd.concat([df_out, df_all[df_all['电话'] == i]])

number_list = df_user['电话'].tolist()
for i in range(len(number_list)):
    number_list[i] = str(number_list[i])
# print(type(number_list[0]))
# number_list = ['13571546550']
df_all = df_all[df_all['电话'].isin(number_list)]
print(df_all)

writer = pd.ExcelWriter('筛选用户电话记录.xlsx')
df_all.to_excel(writer, index=False)
writer.save()
