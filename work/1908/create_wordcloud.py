from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from pylab import mpl

# mpl.rcParams['font.sans-serif'] = ['SimHei']  # 防止乱码

text = open(r'D:\数据\电话医生\老年人主诉.txt', 'r', encoding='utf-8').read()
jieba.del_word('问题')
jieba.del_word('舒服')
jieba.del_word('有点')
jieba.del_word('什么')
jieba.del_word('不好')
jieba.del_word('女士')
jieba.del_word('女性')
jieba.del_word('女孩')
jieba.del_word('男士')
jieba.del_word('先生')
jieba.del_word('男性')
jieba.del_word('男孩')
jieba.del_word('待查')
jieba.del_word('原因')
jieba.del_word('现在')
jieba.del_word('咨询')
jieba.del_word('孩子')
jieba.del_word('宝宝')
jieba.del_word('半月')
jieba.del_word('新生')
jieba.del_word('新生儿')
jieba.del_word('生儿')
jieba.del_word('小孩')
jieba.del_word('孩子')

cut = jieba.cut(text)

text = ' '.join(cut)

wc = WordCloud(
    font_path='simhei.ttf',  # 字体路劲
    background_color='white',  # 背景颜色
    width=600,
    height=340,
    max_font_size=130,  # 字体大小
    min_font_size=10,
    max_words=100,
    scale=1.5,  # 放大1.5倍
    prefer_horizontal=1,
    # mask=plt.imread('xin.jpg'),  # 背景图片
    repeat=True
)


wc.generate(text)
wc.to_file('主诉云图.png')

plt.figure('WordCloud', dpi=200)  # 图片显示的名字
plt.imshow(wc)
plt.axis('off')  # 关闭坐标

plt.savefig('主诉云图.png', dpi=200)
plt.show()
