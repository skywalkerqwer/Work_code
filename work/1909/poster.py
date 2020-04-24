import pandas as pd

PATH = r'C:\Users\Healthlink\Desktop\\'
FILE = '北京国寿心电宝检测营销员海报2019_09_26'

df = pd.read_csv(PATH+FILE+'.csv',engine='python')


def do(s):
    s = str(s)
    return s.strip()

for index,row in df.iteritems():
    df[index] = df[index].apply(do)

df.to_excel('输出'+FILE+'.xls',index=False)
