"""
数据清洗简单工具
"""
import pandas as pd
import numpy as np


def get_df(path):
    """
    读取excel或csv文件
    :param path: 文件路径
    :return: Dataframe对象
    """
    try:
        df = pd.read_excel(path)
    except:
        df = pd.read_csv(path, engine='python')
    return df


def regu_date(x):
    s = str(x)
    s = s[0:9]
    return s


def get_regu_date(df):
    df['date'] = df['date'].apply(regu_date)
    return df


def save_excel(df, path):
    writer = pd.ExcelWriter(path)
    df.to_excel(writer, index=False)
    writer.save()


if __name__ == '__main__':
    PATH = r''
    FILE = r''
    df = get_df(PATH + FILE)
    df = get_regu_date(df)
    count_se = df.value_counts()
    save_excel(count_se, PATH+FILE)