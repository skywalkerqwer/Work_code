"""
用户高频问题及医生诊断
"""
import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

male_question = open(r'male_question.txt', 'r', encoding='gbk').read()
male_answer = open(r'male_answer.txt', 'r', encoding='gbk').read()
female_question = open(r'female_question.txt', 'r', encoding='gbk').read()
female_answer = open(r'female_answer.txt', 'r', encoding='gbk').read()

jieba.del_word('问题')
jieba.del_word('舒服')
jieba.del_word('有点')
jieba.del_word('什么')
jieba.del_word('不好')
jieba.del_word('女士')
jieba.del_word('女性')
jieba.del_word('女孩')
jieba.del_word('男士')
jieba.del_word('男性')
jieba.del_word('男孩')
jieba.del_word('待查')
jieba.del_word('怎么')

cut = jieba.cut(male_question)
male_question = ' '.join(cut)

cut = jieba.cut(male_answer)
male_answer = ' '.join(cut)

cut = jieba.cut(female_question)
female_question = ' '.join(cut)

cut = jieba.cut(female_answer)
female_answer = ' '.join(cut)


wc = WordCloud(
    font_path='simhei.ttf',  # 字体路劲
    background_color='white',  # 背景颜色
    width=400,
    height=400,
    max_font_size=100,  # 字体大小
    min_font_size=10,
    max_words=50,
    scale=1.5,  # 放大1.5倍
    # mask=plt.imread('xin.jpg'),  # 背景图片
)

wc.generate(male_question)
plt.figure('Male questions')
plt.title('Male questions')
plt.imshow(wc)
plt.axis('off')
plt.savefig('Male questions', dpi=600)

wc.generate(male_answer)
plt.figure('Male answer')
plt.title('Male answer')
plt.imshow(wc)
plt.axis('off')
plt.savefig('Male answer', dpi=600)

wc.generate(female_question)
plt.figure('Female questions')
plt.title('Female questions')
plt.imshow(wc)
plt.axis('off')
plt.savefig('Female questions', dpi=600)

wc.generate(female_answer)
plt.figure('Female answer')
plt.title('Female answer')
plt.imshow(wc)
plt.axis('off')
plt.savefig('Female answer', dpi=600)

plt.show()


