import pandas as pd

PATH = r'C:\Users\Healthlink\Desktop\\'
FILE = 'poster-国寿臻心七十载 庆典钜献福临门营销员海报2019-12-09'

print('开始读取')

df = pd.read_csv(PATH+FILE+'.csv',engine='python')
print('读取完成')
df = df.drop([0])  # 删除备注行

def do(s):
    s = str(s)
    return s.strip()

for index,row in df.iteritems():
    df[index] = df[index].apply(do)
    print('处理完成：', index)

df['员工备案数据\t'] = df['员工备案数据\t'].astype('int32')
df['员工登录数据\t'] = df['员工登录数据\t'].astype('int32')
df['员工海报数据\t'] = df['员工海报数据\t'].astype('int32')


# df.to_excel('输出--'+FILE+'.xlsx',index=False)
