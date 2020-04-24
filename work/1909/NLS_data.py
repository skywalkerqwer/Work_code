import pandas as pd
import time

t1 = time.time()

print('开始读取')
df1 = pd.read_excel(r'D:\数据\基因系统\数据提取\NLS机构微磁检测数据.xlsx', sheet_name='NLS机构微磁检测数据1')
print('完成：sheet1')
df2 = pd.read_excel(r'D:\数据\基因系统\数据提取\NLS机构微磁检测数据.xlsx', sheet_name='NLS机构微磁检测数据2')
print('完成：sheet2')
df3 = pd.read_excel(r'D:\数据\基因系统\数据提取\NLS机构微磁检测数据.xlsx', sheet_name='NLS机构微磁检测数据3')
print('完成：sheet3')
df4 = pd.read_excel(r'D:\数据\基因系统\数据提取\NLS机构微磁检测数据.xlsx', sheet_name='NLS机构微磁检测数据4')
print('完成：sheet4')
df5 = pd.read_excel(r'D:\数据\基因系统\数据提取\NLS机构微磁检测数据.xlsx', sheet_name='NLS机构微磁检测数据5')
print('完成：sheet5')
t2 = time.time()
print('读取完成,耗时：',t2-t1)

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
    try:
        s = d[i]
    except:
        s = '异常'
    return s


for d in [df1, df2, df3, df4, df5]:
    d['年龄分段'] = d['用户年龄'].transform(divide_age)

t3 = time.time()
print('处理完成耗时：', t3-t2)

writer = pd.ExcelWriter('年龄分段-NLS机构微磁检测数据.xlsx')

for i, d in enumerate([df1, df2, df3, df4, df5]):
    d.to_excel(writer, 'NLS机构微磁检测数据'+str(i), index=False)
writer.save()

print('总耗时：', time.time()-t1)
