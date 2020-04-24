"""
生成慢病报告6大风险云图
"""
from wordcloud import WordCloud

with open('report.txt', 'a') as f:
    print('start')
    s1 = '高血压\n'*518
    s2 = '糖尿病\n'*163
    s3 = '猝死\n'*69
    s4 = '慢性阻塞性肺部疾病\n'*62
    s5 = '心肌梗塞\n'*52
    s6 = '肺部原发性恶性肿瘤\n'*12
    f.write(s1)
    f.write(s2)
    f.write(s3)
    f.write(s4)
    f.write(s5)
    f.write(s6)

text = open(r'D:\数据\慢病QA数据\report.txt', 'r', encoding='utf-8').read()


wc = WordCloud(
    font_path='simhei.ttf',  # 字体路劲
    background_color='white',  # 背景颜色
    width=500,
    height=300,
    max_font_size=600,  # 字体大小
    min_font_size=10,
    max_words=6,
    scale=1.5,  # 放大1.5倍
    prefer_horizontal=1,
    # mask=plt.imread('xin.jpg'),  # 背景图片
    repeat=False,
    collocations=False,
)


wc.generate(text)
wc.to_file('report.png')