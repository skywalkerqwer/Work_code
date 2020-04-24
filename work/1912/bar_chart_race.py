import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 防止乱码

# df = pd.read_excel(r'D:\数据\1.xlsx')
df = pd.read_excel(r'D:\数据\2019年全量业务数据\2019挂号服务情况.xlsx')


# 整理数据
def get_date(s):
    s = str(s)
    s = s[0:7]
    return s


df['date'] = df['date'].apply(get_date)
# df_group = df.groupby(['date','产品'])  # 先按日期再按产品分类
# df_group = df_group.size()  # 统计
# print(df_group)

# writer = pd.ExcelWriter('3.xlsx')
# df_group.to_excel(writer)
# writer.save()
# 统计了每年每个产品的使用次数，但需要统计每年的产品累计使用次数

df['date'] = df['date'].astype('datetime64')
df = df.set_index('date')  # 设置时间索引
df = df.sort_index()  # truncate方法必须先将索引进行排序

df_all = pd.DataFrame()

for year in range(2013, 2020):
    for month in range(1, 13):
        date = str(year) + '-' + str(month)
        # truncate按照日期进行切片
        df_temp = df.truncate(after=date)
        count = df_temp['产品名称'].value_counts().head(10)
        # series转换为 dataframe 先取得索引和值构建字典，再用字典创建df
        dict_count = {'name': count.index, 'value': count.values}
        df_count = pd.DataFrame(dict_count)
        # 添加date字段
        df_count['date'] = date
        df_all = pd.concat([df_all, df_count], axis=0)

print(df_all)

colors = dict(zip(
    ['平安电销北京增值服务续保', '平安健康安心卡2013', '平安电销北京增值服务续保', '远盟BY CASE 结算案例',
     '太平人寿健康管理钻石服务', '平安电销续保服务2013', '集中采购苏州国寿', '太平人寿税优转诊导医服务',
     '太平人寿重疾2019版单人卡一', '中意人寿高端预约挂号项目', '太平财北分健康救援服务', '中意人寿股东项目转诊导医服务',
     '捷越联合回馈升级陪诊导医服务', '集中采购苏州国寿2017', '永诚财险高端就医服务', '光大乐容计划',
     '平安健康险健康无忧卡', '平安健康安心卡', '太保北分普通客户', '12孝行天下卡（无陪诊无体检）',
     '英大车险人伤报送服务', '未知', '平安关爱行B款', '国航常旅客',
     '太平洋财险北分优享汇', '乐途亿佰百灵卡', '国寿健康绿色通道', '福瑞幸福养老平安卡',
     '平安国内紧急医疗救援卡', '太平人寿VIP', '合众人寿总重疾服务', '集中采购北京国寿',
     '中意VIP增值服务', '太平人寿健康管理铂金服务', '太平人寿健康管理黄金服务', '国寿北分健康管家',
     '国寿北分集采项目2014', '安心财水滴百万医疗服务', '华夏转诊导医服务', '德国通再中英咨询重疾服务',
     '阳光人寿紧急救援服务', '水滴保健康咨询增值服务', '华泰财健康管理服务', '捷越联合个性化服务',
     '新华卓越重疾绿通服务',
     ],
    ['#adb0ff', '#ffb3ff', '#90d595', '#e48381',
     '#aafbff', '#f7bb5f', '#eafb50', "#918597",
     "#6950a1", "#1d953f", "#ac6767", "#b2d235",
     "#b2d235", "#b2d235", "#b2d235", "#b2d235",
     "#b2d235", "#b2d235", "#b2d235", "#b2d235",
     "#b2d235", "#b2d235", "#b2d235", "#b2d235",
     "#b2d235", "#b2d235", "#b2d235", "#b2d235",
     "#b2d235", "#b2d235", "#b2d235", "#b2d235",
     "#b2d235", "#b2d235", "#b2d235", "#b2d235",
     "#b2d235", "#b2d235", "#b2d235", "#b2d235",
     "#b2d235", "#b2d235", "#b2d235", "#b2d235",
     "#b2d235",
     ]
))


fig, ax = plt.subplots(figsize=(11, 7))
for name in df_all['name']:
    if name not in colors:
        colors[name] = "#b2d235"

# 2019重疾修改部分
colors['太平人寿健康管理铂金服务'] = '#adb0ff'
colors['新华卓越重疾绿通服务'] = '#ffb3ff'
colors['太平人寿健康管理黄金服务'] = '#90d595'
colors['水滴保健康咨询增值服务'] = '#eafb50'
colors['安心财水滴百万医疗服务'] = '#aafbff'
colors['华泰财健康管理服务'] = '#AB26E4'
colors['国寿总部各县境内绿通VIP白金卡'] = '#D68E3B'
# 2019挂号修改部分
colors['华夏转诊导医服务'] = '#f7bb5f'
colors['捷越联合回馈升级陪诊导医服务'] = '#eafb50'
colors['中信保诚人寿健康管理服务'] = '#444693'
colors['中意人寿股东项目转诊导医服务'] = '#f05b72'
colors['PICC北分陪诊导医服务'] = '#2FC9BC'
colors['太平养老深分指定挂号服务'] = '#5885D6'
colors['太平人寿转诊导医服务'] = '#49D3A6'

def draw_barchart(date):
    dff = df_all[df_all['date'].eq(date)].sort_values(by='value', ascending=True).tail(10)
    ax.clear()

    ax.barh(dff['name'], dff['value'], color=[colors[x] for x in dff['name']])
    # ax.barh(dff['name'], dff['value'])

    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value, i, name, size=12, weight=600, ha='right')
        ax.text(value, i,     f'{value:,.0f}',  size=14, ha='left', color='#ff0000')
    ax.text(1, 0.4, date, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'Service use', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.1, 'The most use service from 2013 to 2019',
            transform=ax.transAxes, size=24, weight=600, ha='left')
    plt.box(False)


def date_range():
    for year in range(2019, 2020):
        for month in range(1, 13):
            if year == 2013:
                if month < 7:
                    continue
            # if year == 2019:
            #     if month == 8:
            #         break
            date = str(year) + '-' + str(month)
            yield date

plt.rcParams["animation.convert_path"] = "C:\ProgramFiles\ImageMagick\magick.exe"

animator = animation.FuncAnimation(fig, draw_barchart, frames=date_range(), interval=3)
# Writer = animation.writers['ffmpeg']
# animator.save('re.gif', writer='ffmpeg',dpi=500)

animator.save('挂号.gif', writer='imagemagick', extra_args="convert")
# plt.show()
