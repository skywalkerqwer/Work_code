import pandas as pd
import jieba

text = open(r'D:\数据\电话医生\老年人主诉.txt', 'r', encoding='utf-8').read()

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
writer = pd.ExcelWriter('词频.xlsx')
freq_df.to_excel(writer)
writer.save()
