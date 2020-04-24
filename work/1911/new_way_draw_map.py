import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map

PATH = r'D:\数据\电话医生\\'
FILE = '咨询量2019.xlsx'
df = pd.read_excel(PATH + FILE)

# 获取全国各省份来电量分布
province_num = df['来电省份'].value_counts()
province_num_list = [list(i) for i in province_num.items()]
# print(province_num_list)  # [['上海', 8611], ['四川', 7995], ['北京', 7450],...]

# 生成热力图
province_num_map = (
    Map()
    .add("2019来电地图", province_num_list, "china")
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=12399))
)

province_num_map.render('calling-number-map.html')
