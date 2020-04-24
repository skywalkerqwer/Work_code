import pandas as pd
df = pd.read_excel(r'C:\Users\Healthlink\Desktop\数据\电话3-8.xlsx')
df = pd.value_counts(df['电话'])
df.to_excel('freq.xls')
