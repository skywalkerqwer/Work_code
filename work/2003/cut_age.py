"""
一种划分连续数值的方式
"""
import pandas as pd
import numpy as np


df = pd.read_excel(r'D:\数据\电话医生\健康咨询结构化数据.xlsx', sheet_name='Sheet1')

cut_bins = np.arange(0, 100 , 5)  # 从0到100每5分一段

bins = pd.cut(df['年龄'], cut_bins)

bin_counts = df['年龄'].groupby(bins).count()
print(bin_counts)
