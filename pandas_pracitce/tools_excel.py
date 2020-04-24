"""
自定义excel工具
"""

import pandas as pd
import os
import numpy as np


def get_all_sheet(file_path=None):
    """
    读取excel中所有sheet，返回列表，每个元素为一个sheet
    """
    dfs = []
    i = 0
    while True:
        try:
            dfs.append(pd.read_excel(file_path, sheet_name=i))
            i += 1
        except IndexError:
            break
    return dfs


def get_all_excel(path):
    excel_path_list = []
    parents = os.listdir(path)
    for parent in parents:  # 返回指定路径下所有文件和文件夹的名字，并存放于一个列表中
        child = os.path.join(path, parent)
        if os.path.isdir(child):  # 将多个路径组合后返回
            get_all_excel(child)
        elif os.path.isfile(child):  # 如果是目录，则继续遍历子目录的文件
            suffix = os.path.splitext(child)[1]  # 获取后缀名
            if suffix == '.xls' or suffix == '.xlsx':
                excel_path_list.append(child)
    return excel_path_list


def df_to_dict(df):
    """将DataFrame转换为列表嵌套字典
    [{
        key1: value1,
        key2: value2,
    },{
        key1: value1,
        key2: value2,
    }]
    """
    test_data = []
    for i in df.index.values:  # 获取行号的索引，并对其进行遍历：
        # 根据i来获取每一行指定的数据 并利用to_dict转成字典
        row_data = df.loc[i, list(df.keys())].to_dict()
        test_data.append(row_data)
    return test_data


if __name__ == '__main__':
    path_list = get_all_excel(r'D:\Code\pandas_pracitce\test_excel')
    print(path_list)
