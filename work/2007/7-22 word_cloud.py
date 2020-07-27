from wordcloud import WordCloud
import jieba

text = open(r'D:\Work_code\work\2007\1.txt', 'r', encoding='utf-8').read()

jieba.del_word('测试')
jieba.del_word('很好')

cut = jieba.cut(text)
text = ' '.join(cut)



wc = WordCloud(
    font_path='simhei.ttf',  # 字体路劲
    background_color='white',  # 背景颜色
    width=500,
    height=300,
    max_font_size=300,  # 字体大小
    min_font_size=10,
    max_words=10,
    scale=1.5,  # 放大1.5倍
    prefer_horizontal=1,
    # mask=plt.imread('xin.jpg'),  # 背景图片
    repeat=False,
    collocations=False,
)


wc.generate(text)
wc.to_file('report.png')
