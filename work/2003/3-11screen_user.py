"""
从名单中筛选包含其中服务元素的
"""
import pandas as pd

df = pd.read_excel(r'D:\数据\基因微磁数据客户(1).xlsx')
df = df.fillna('na')

df = df[df['服务元素'].str.contains('医疗咨询')]  # 筛选包含字符串的行
# df = df[df['服务元素'].str.contains('院前急救费用垫付\(限境内\)')]  # 括号属于正则公式，需加\转义
df = df[df['服务元素'].str.contains('住院费用垫付')]
df = df[df['服务元素'].str.contains('健康档案')]
# df = df[df['服务元素'].str.contains('国内专家二次诊疗意见5项服务的人员名单')]
# df = df[df['服务元素'].str.contains('自助预约挂号')]
print(df)

writer = pd.ExcelWriter('筛选服务元素-健康档案+住院垫付.xlsx')
df.to_excel(writer, index=False)
writer.save()
