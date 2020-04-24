import pandas as pd
import numpy as np

# 读取拜访活动表
data_cus_act = pd.read_excel(r'C:\Users\Healthlink\Desktop\total_activity01.xlsx')
# 处理LONGLATTIME列
data_cus_act['LONGLATTIME'] = data_cus_act['LONGLATTIME'].apply(lambda x:str(x)[:10].replace('-',''))
# print(data_cus_act.head())

"""
  BUSINESSTYPECODE BUSINESSTYPE MAIN  ...  LONGLATTIME CUSTOMERID CUSTOMERCODE
0              Z99           其他   一般  ...     20180426     590753   0041971840
1              Z05          工业油   重要  ...     20180206    2836598   0046638840
2              Z05          工业油   重要  ...     20180621    1479324   0046196620
"""

weight = {
    'vp_005' : 8,
    'vp_003' : 7,
    'vp_004' : 6,
    'vp_001' : 5,
    'vp_002' : 4,
    'vp_006' : 3,
    'vp_007' : 2,
    'vp_008' : 1,
}

def get_weight(x):
    # x: str
    w = []
    list_s = x.split(',')
    for s in list_s:
        w.append(weight[s])
    return max(w)

data_cus_act['weight'] = data_cus_act['VISITTARGETCODE'].apply(get_weight)
# print(data_cus_act)


df = data_cus_act.groupby(['BUSINESSTYPECODE', 'LONGLATTIME', 'CUSTOMERID'])
df_re = pd.DataFrame(data=None, )
for (k1, k2, k3), group in df:
    # print(k1, k2, k3)
    # print(group)
    max_weight = group['weight'].max()
    max_raw = group[group['weight'] == max_weight]
    print('-'*50)
