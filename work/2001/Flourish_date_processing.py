"""
为Flourish网站做bar_chart_race动态图做数据处理
"""
import pandas as pd
import tools

PATH = r'D:\数据\项目产品数据\\'
FILE = r'挂号服务使用情况--客户.xlsx'

df_origin = pd.read_excel(PATH + FILE)


# 整理数据
def get_date(s):
    s = str(s)
    s = s[0:7]
    return s


df_origin['date'] = df_origin['date'].apply(get_date)
df_origin['date'] = df_origin['date'].astype('datetime64')

def date_range():
    for year in range(2013, 2020):
        for month in range(1, 13):
            if year == 2013:
                if month < 7:
                    continue
            date = str(year) + '-' + str(month)
            yield date


# 构建每个产品的使用明细表
df_out_put = pd.DataFrame()
df_out_put['name'] = df_origin['name'].value_counts().index


for date in date_range():
    # print(date)
    # 按日期逐步筛选
    df_count_temp = df_origin[df_origin['date'] <= date]
    # print('df_count_temp:', df_count_temp)
    se_count = df_count_temp['name'].value_counts()
    # print('se_count:', se_count)
    # series转换为DF
    dict_count = {'name': se_count.index, date: se_count.values}
    df_count = pd.DataFrame(dict_count)
    # print('df_count:', df_count)
    # 拼接
    df_out_count = pd.merge(df_out_put, df_count, how='left')
    # print('df_out_count', df_out_count)
    df_out_put[date] = df_out_count[date]
    # print('df_out_put', df_out_put)
    # break

df_out_put = df_out_put.fillna(0)
tools.save_excel(df_out_put, PATH+'Flourish 预处理数据.xlsx')
