"""
挑选出拨打电话咨询的营销员记录
"""
import pandas as pd

df_user = pd.read_excel(r'D:\Code\work\2007\营销员信息2017年数据.xlsx')
df_all = pd.read_excel(r'D:\Code\work\2007\医生.xlsx')


number_list = df_user['营销员电话'].tolist()
for i in range(len(number_list)):
    number_list[i] = str(number_list[i])

df_all = df_all[df_all['电话'].isin(number_list)]
# print(df_all)

writer = pd.ExcelWriter('17年营销员电话记录.xlsx')
df_all.to_excel(writer, index=False)
writer.save()
