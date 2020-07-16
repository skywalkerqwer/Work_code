"""
一种划分连续数值的方式
"""
import pandas as pd
import numpy as np


df1 = pd.read_excel(r'D:\数据\其他\珊瑚取关用户数据.xlsx', sheet_name='取关注册用户')
df2 = pd.read_excel(r'D:\数据\其他\珊瑚取关用户数据.xlsx', sheet_name='取关激活用户')

cut_bins = np.arange(0, 100 , 5)  # 从0到100每5分一段

bins1 = pd.cut(df1['年龄'], cut_bins)
bin_counts1 = df1['年龄'].groupby(bins1).count()

bins2 = pd.cut(df2['年龄'], cut_bins)
bin_counts2 = df2['年龄'].groupby(bins2).count()

print(bin_counts1)
print("==========")
print(bin_counts2)


writer = pd.ExcelWriter('年龄分段.xlsx')
bin_counts1.to_excel(writer,index=True, sheet_name='取关注册用户')
bin_counts2.to_excel(writer,index=True, sheet_name='取关激活用户')
writer.save()
