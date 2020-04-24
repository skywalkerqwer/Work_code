"""
统计文本中单词的出现频率
"""

import pandas as pd
import jieba

text = open(r'D:\Code\work\2003\记录.txt', 'r', encoding='utf-8').read()

cut = jieba.cut(text)

text = ' '.join(cut)

print(text)

freq = {'频率': {}}

for word in text.split():
    if word not in freq['频率']:
        freq['频率'][word] = 1
    else:
        freq['频率'][word] += 1

freq_df = pd.DataFrame(freq)
writer = pd.ExcelWriter('水滴记录词频统计.xlsx')
freq_df.to_excel(writer)
writer.save()
