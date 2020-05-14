"""
    分析答题时间
    答题间隔时间，单位：天
"""
import pandas as pd

PATH = r'D:\数据\慢病QA数据\提取\\'
FILE = '慢病用户问答数据2020-05-11.xlsx'

origin_df = pd.read_excel(PATH + FILE)  # 原始数据

valid_ans_df = origin_df.dropna(axis=0, subset=['问题1'])

answer_time = valid_ans_df[['问题'+str(i)+'答案时间' for i in range(1, 51)]]
answer_time = answer_time.astype('datetime64')


# 根据最早答题和最后答题时间差计算答题间隔时间
ans_time_df = pd.DataFrame()
ans_time_df['姓名'] = valid_ans_df['姓名']
ans_time_df['身份证号'] = valid_ans_df['身份证号']
ans_time_df['最早答题时间'] = answer_time.min(axis=1)
ans_time_df['最后答题时间'] = answer_time.max(axis=1)
ans_time_df['答题间隔天数'] = ans_time_df['最后答题时间'] - ans_time_df['最早答题时间']
print(ans_time_df)
writer = pd.ExcelWriter('答题时间分析--' + FILE)
ans_time_df.to_excel(writer)
writer.save()
