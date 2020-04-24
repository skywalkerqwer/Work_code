"""
气泡动画
"""
import matplotlib.pyplot as mp
import matplotlib.animation as ma
import numpy as np

# 构建100个泡泡,整理他们的属性字段
n = 100
balls = np.zeros(n, dtype=[
    ('position', float, 2),
    ('size', float, 1),
    ('growth', float, 1),
    ('color', float, 4),
])

# 初始化所有ball的属性
# 初始化所有ball的坐标 uniform --> 平均分布
balls['position'] = np.random.uniform(0, 1, (n, 2))  # 随机生成最小值为0最大值为1的n行2列的数组
# 初始化ball大小
balls['size'] = np.random.uniform(40, 70, n)
# 初始化ball生长速度
balls['growth'] = np.random.uniform(10, 20, n)
# 初始化ball颜色
balls['color'] = np.random.uniform(0, 1, (n, 4))

# 画图
mp.figure('Animation', facecolor='lightgray')
mp.title('Animation', fontsize=16)
# 隐藏刻度文本
mp.xticks([])
mp.yticks([])

sc = mp.scatter(
    balls['position'][:, 0],  # x坐标
    balls['position'][:, 1],  # y坐标
    s=balls['size'],
    color=balls['color'],
)


def update(number):
    """更新图像"""
    balls['size'] += balls['growth']
    # 让某个球重新初始化
    i = number % n
    balls[i]['size'] = np.random.uniform(40, 70, 1)
    balls[i]['position'] = np.random.uniform(0, 1, (1, 2))
    # 改变大小
    sc.set_sizes(balls['size'])  # sc为所画的对象
    # 改变位置
    sc.set_offsets(balls['position'])
    print('update:',number)


# 需要有变量接受返回值
anim = ma.FuncAnimation(mp.gcf(), update, interval=15)  # interval 帧与帧之间的延迟  FPS = 1000/interval  =  66.7Hz

mp.show()
