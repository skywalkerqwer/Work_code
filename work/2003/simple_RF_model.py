"""
简陋的RF模型
对电话记录进行分值计算
"""

import pandas as pd

# df = pd.read_excel(r'D:\数据\电话医生\3-30电话医生服务客户信息.xlsx')
df = pd.read_excel(r'D:\Code\work\2003\3-30电话医生间隔计算.xlsx')

# 计算最后来电距今时间
# df['现在'] = df['现在'].astype('datetime64')
# df['最近一次来电时间'] = df['最近一次来电时间'].astype('datetime64')
# df['距今时间'] = df['现在'] - df['最近一次来电时间']

# 分值计算
df['来电次数-SCORE'] = pd.cut(df['来电次数'], bins=[0, 10, 20, 30, 40, 50, 1000000], labels=[1, 2, 3, 4, 5, 6], right=False).astype(float)
df['距今时间-SCORE'] = pd.cut(df['距今时间'], bins=[0, 14, 30, 60, 180, 1000000], labels=[5, 4, 3, 2, 1], right=False).astype(float)

writer = pd.ExcelWriter('3-30电话医生间隔计算.xlsx')
df.to_excel(writer, index=False)
writer.save()
