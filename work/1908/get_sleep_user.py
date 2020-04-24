"""
获取沉默用户
"""
import pandas as pd

user = pd.read_excel(r'C:\Users\Healthlink\Desktop\数据\电话3-8.xlsx')

all_user = pd.read_excel(r'C:\Users\Healthlink\Desktop\数据\中医检测活动数据\天津卡激活数据提取.xls')

user = user.drop_duplicates(subset='姓名')

for i in user.index:
    try:
        all_user.drop(all_user[all_user['用户名']==user['姓名'][i]].index, axis=0, inplace=True)
    except:
        pass

all_user.to_excel('沉默用户.xls')
