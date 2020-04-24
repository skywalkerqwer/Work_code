"""
短信使用量预测
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as plt

# 基于岭回归的模型
data = np.loadtxt()
x = data[:, :-1]
y = data[:, -1]

# 创建线性回归模型
model = lm.LinearRegression()
# 训练模型
model.fit(x, y)
# 根据输入预测输出
pred_y1 = model.predict(x)
# 创建岭回归模型
model = lm.Ridge(150, fit_intercept=True, max_iter=10000)
# 训练模型
model.fit(x, y)
# 根据输入预测输出d17w
pred_y2 = model.predict(x)
