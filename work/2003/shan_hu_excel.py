import os
import pandas as pd
from string import digits
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 5000)

# 将一个excel中多个sheet合并位一个df
df_content = pd.concat(pd.read_excel(r'D:\数据\内容文章\所有内容.xlsx', sheet_name=None), ignore_index=True)
# 构建输出df
df_out = pd.DataFrame(columns=['标题', '简介', '类型(1紧急自救卡，2家庭保健卡)', '标签', '头图名称', '长图文名称', '排序'])
df_head = pd.DataFrame(columns=['头图名称'])
df = pd.DataFrame(df_out)

def stand_name(x):
    # 将文件名还原为标题名
    if x.count('.') == 1:
        return x.split('-')[-1].split('.')[0]
    if x.count('.') == 2:
        return x.split('.', maxsplit=-1)[1]

def stand_label(x):
    # 标签去除“-”和数字
    x = x.replace('-', '')
    remove_digits = str.maketrans('', '', digits)
    return x.translate(remove_digits)

def get_head(x):
    x = ''.join(x.split())
    return x.split('。')[0]


for root, dirs, files in os.walk('D:\数据\内容文章\珊瑚健康-长图文'):
    # print("root:", root)  # 当前目录路径
    # print("dirs:", dirs)  # 当前路径下所有子目录
    # print("files:", files)  # 当前路径下所有非目录子文件
    if root.split('\\')[-1] == '长图':
        dic = {
            '标签' : root.split('\\')[-2],
            '长图文名称' : files
        }
        df_temp = pd.DataFrame(dic)
        # print(df_temp)
        df_out = pd.concat([df_out, df_temp], sort=True ,ignore_index=True)

    if root.split('\\')[-1] == '缩略图':
        dic2 = {
            '头图名称' : files
        }
        df_head_temp = pd.DataFrame(dic2)
        df_head = pd.concat([df_head, df_head_temp], sort=True ,ignore_index=True)

df_head_info = pd.merge(df_out, df_head, how='left', left_on='长图文名称', right_on='头图名称')
df_out['头图名称'] = df_head_info['头图名称_y']

df_out = df_out.drop_duplicates(subset='长图文名称', keep='first')
df_out = df_out.reset_index(drop=True)


df_out['标题'] = df_out['长图文名称'].apply(stand_name)
df_out['标签'] = df_out['标签'].apply(stand_label)
df_content['简介'] = df_content['简介'].apply(get_head)
df_out = pd.merge(df_out, df_content, how='left', left_on='标题', right_on='标题')
df_out = df_out.drop_duplicates(subset='长图文名称', keep='first')
df_out = df_out.reset_index(drop=True)

df['标题'] = df_out['标题']
df['简介'] = df_out['简介_y']
df['类型(1紧急自救卡，2家庭保健卡)'] = '1'
df['标签'] = df_out['标签']
df['头图名称'] = df_out['头图名称']
df['长图文名称'] = df_out['长图文名称']
# df['排序'] = df_out['排序']
print(df)
writer = pd.ExcelWriter('急救知识明细.xlsx')
df.to_excel(writer, index=False)
writer.save()
