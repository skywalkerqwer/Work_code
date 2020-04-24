import pandas as pd

df = pd.read_excel(r'D:\数据\电话医生\健康咨询服务时间.xlsx', sheet_name='新')


def s_date(s):
    try:
        s = str(s)
        year = s[0:4]
        return int(year)
    except BaseException:
        return 'error'


"""
2019  1 31 23 51 00680
2018 12 22 20 57 09803
2018 11 26 19 48 02965
"""


def get_start_time(s):
    s = str(s)
    if len(s) == 16:
        s_l = list(s)
        s_l.insert(4, '0')
        s = ''.join(s_l)
    hour = int(s[8:10])
    minutes = int(s[10:12])
    sec = int(s[12:14])
    return hour * 3600 + 60 * minutes + sec


def get_end_time(s):
    try:
        s = str(s)
        hour = int(s[11:13])
        minutes = int(s[14:16])
        sec = int(s[17:19])
        return hour * 3600 + 60 * minutes + sec
    except BaseException:
        return 0


df['年'] = df['服务时间'].apply(s_date)
df['start'] = df['来电编码'].apply(get_start_time)
df['end'] = df['服务时间'].apply(get_end_time)
df['use'] = df['end'] - df['start']

df_2018 = df[df['年'] == 2018]
df_2019 = df[df['年'] == 2019]

writer = pd.ExcelWriter('服务时间.xlsx')
df_2018.to_excel(writer, sheet_name='2018', index=False)
df_2019.to_excel(writer, sheet_name='2019', index=False)
writer.save()
