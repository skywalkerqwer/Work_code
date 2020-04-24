import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map

PATH = r'D:\数据\慢病QA数据\提取\\'
FILE = '慢病用户问答数据2019-11-11.xlsx'
origin_df = pd.read_excel(PATH + FILE)


with open('D:\Code\work\data\id_area.txt', 'r', encoding='UTF-8') as f:
    area = eval(f.read())


def get_area(x):
    code = x[:2]
    code = code + '0000'
    result = area[code]
    if '市' in result:
        return result.replace('市', '')
    elif '省' in result:
        return result.replace("省", '')
    elif "自治区" in result:
        if '内蒙古' in result:
            return '内蒙古'
        else:
            return result[0:2]


area_df = pd.DataFrame()
area_df['身份证号'] = origin_df['身份证号']
area_df['省份'] = area_df['身份证号'].apply(get_area)
# 获取全国各省份数量分布
province_num = area_df['省份'].value_counts()
province_num_list = [list(i) for i in province_num.items()]
print(province_num_list)

# 生成热力图
province_num_map = (
    Map()
    .add("问卷评估用户全国分布", province_num_list, "china")
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=4640, type_='color'))
)

province_num_map.render('QA-map.html')
