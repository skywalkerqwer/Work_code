"""
KPI模型计算
"""
import numpy as np
import pandas as pd
p1 = np.arange(0.00, 1.00, 0.01)
p1 = p1.tolist()
p2 = p1
p3 = p1

X = []
Y = []
Z = []
val = []

for i, x in enumerate(p1):
    i = i * 10000
    for j, y in enumerate(p2):
        j = j * 100
        for k, z in enumerate(p3):
            print('当前进度：第%d组合' % (i+j+k))
            if 0.95 <= (x + y + z) <= 1:
                X.append(x)
                Y.append(y)
                Z.append(z)
                val.append(x + 2*y + 3*z)
            else:
                continue

dict = {'P1': X, 'P2': Y, 'P3': Z, 'val':val}
df = pd.DataFrame(dict)
dff = df[df['val'] >= 1.5]

writer = pd.ExcelWriter('kpi_model.xlsx')
dff.to_excel(writer, index=False)
writer.save()
