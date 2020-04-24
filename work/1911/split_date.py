import pandas as pd

df = pd.read_excel(r'D:\数据\电话医生\健康咨询服务时间.xlsx', sheet_name='总')


def s_date(s):
    try:
        s = str(s)
        re_year = s[0:4]
        return int(re_year)
    except BaseException:
        return 'error'


df['年'] = df['服务时间'].apply(s_date)
print('show:', df)

df_2015 = df[df['年'] == 2015]
df_2016 = df[df['年'] == 2016]
df_2017 = df[df['年'] == 2017]
df_2018 = df[df['年'] == 2018]
df_2019 = df[df['年'] == 2019]

count_df = pd.DataFrame({'年': ['2015', '2016', '2017', '2018', '2019'],
                         '人数': [0, 0, 0, 0, 0]})
for i in range(5):
    year = 2015 + i
    d = 'df_' + str(year)
    d = eval(d)
    d = d.drop_duplicates('电话')
    print(d)
    count = d.count()
    print(count)
    count_df.loc[i:i + 1, '人数'] = count.loc['电话']
    print('===========')

writer = pd.ExcelWriter('服务时间.xlsx')
count_df.to_excel(writer, index=False)
writer.save()
