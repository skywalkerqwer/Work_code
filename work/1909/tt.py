import pandas as pd


PATH = r'D:\数据\慢病QA数据\提取\\'
FILE = '慢病用户问答数据2019-10-14.xlsx'

origin = pd.read_excel(PATH + FILE)  # 原始数据
answer = pd.Series()
for i in range(1, 91):
    ss = origin['影响因素'+str(i)]
    answer = pd.concat([answer, ss], axis=1)

answer = answer.dropna()
writer = pd.ExcelWriter('影响因素.xlsx')
answer.to_excel(writer)
writer.save()