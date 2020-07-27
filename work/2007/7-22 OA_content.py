import pandas as pd

df = pd.read_excel(r'D:\数据\项目产品数据\7-22\OA.xlsx')

df = df[df['审批人'] == '张红']

def do(x):
    return x.split('>')[-1]

df['上线产品名称'] = df['审批意见'].apply(do)

writer = pd.ExcelWriter('OA产品提取.xlsx')
df.to_excel(writer, index=False)
writer.save()
