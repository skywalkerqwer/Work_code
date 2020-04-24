import pandas as pd
import math

# df = pd.read_excel(r'D:\数据\电话医生\健康咨询(2015-2019）.xlsx')
df = pd.read_excel(r'D:\数据\基因系统\数据提取\北理化机构基因检测数据.xlsx')


def int_age(x):
    # 年龄取整
    tail, head = math.modf(x)
    if tail >= 0.5:
        tail = 1
    else:
        tail = 0
    x = head + tail
    return x


def round_age(x):
    # 年龄四舍五入
    head = x // 10
    temp = (x % 10) // 5
    x = (head + temp) * 10
    return x


def divide_age(x):
    d = {
        2: '0-5',
        7: '5-10',
        12: '10-15',
        17: '15-20',
        22: '20-25',
        27: '25-30',
        32: '30-35',
        37: '35-40',
        42: '40-45',
        47: '45-50',
        52: '50-55',
        57: '55-60',
        62: '60-65',
        67: '65-70',
        72: '70-75',
        77: '75-80',
        82: '80-85',
        87: '85-90',
        92: '90-95',
        97: '95-100',
        102: '100-105',
    }
    i = x//5
    i = i*5 + 2
    return d[i]


def age_step(x):
    x = int(x)
    if x <= 6:
        x = '童年'
    elif x <= 17:
        x = '少年'
    elif x <= 44:
        x = "青年"
    elif x <= 59:
        x = "中年人"
    elif x <= 74:
        x = '年期老年人'
    elif x <= 89:
        x = "老年人"
    else:
        x = '长寿老人'
    return x


# df['年龄'] = df['年龄'].transform(int_age)
# df['年龄'].astype('int')
# df['年龄阶段'] = df['年龄']
df['年龄分段'] = df['用户年龄'].transform(divide_age)
# df['年龄阶段'].astype('str')
# df['年龄阶段'] = df['年龄阶段'].transform(age_step)

writer = pd.ExcelWriter('年龄分段-北理化机构基因检测数据.xlsx')
df.to_excel(writer,index=False)
writer.save()
