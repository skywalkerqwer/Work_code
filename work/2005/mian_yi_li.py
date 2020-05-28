"""
    免疫早早筛表格处理
"""
import pandas as pd

df1 = pd.read_excel(r'D:\数据\5-21 免疫早早筛数据统计分析\支公司统计.xlsx')
df2 = pd.read_excel(r'D:\数据\5-21 免疫早早筛数据统计分析\支公司统计.xlsx', sheet_name='Sheet2')

grouped1 = df1.groupby(['支公司名称'])
dff1 = grouped1.mean()
# grouped2 = df2.groupby(['支公司名称'])
# dff2 = grouped2.count()

writer = pd.ExcelWriter('支公司统计结果.xlsx')
dff1.to_excel(writer, sheet_name='Sheet1')
# dff2.to_excel(writer, sheet_name='Sheet2')
writer.save()