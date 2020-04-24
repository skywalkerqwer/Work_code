import copy
import random
import os
import platform

now_system = platform.system()
if now_system == 'Linux':
    clear = 'clear'
else:
    clear = 'cls'


def atlas(list_total):
    """打印游戏图像"""
    os.system(clear)
    for i in range(len(list_total)):
        for j in range(len(list_total[i])):
            print("%4d" % list_total[i][j], end='  ')
        print('\n')


def zero_to_end(list_target):
    """将列表中0移动到最后"""
    for item in list_target:
        if item == 0:
            list_target.remove(0)
            list_target.append(item)
    return list_target


def merge(list_target):
    """合并列表中两个相邻元素"""
    list_target = zero_to_end(list_target)
    for i in range(len(list_target) - 1):
        if list_target[i] != 0 and list_target[i] == list_target[i + 1]:
            list_target[i] += list_target[i + 1]
            list_target[i + 1] = 0
    list_target = zero_to_end(list_target)
    return list_target


def move_up(atlas):
    """上移"""
    for i in range(4):
        list_merge = []
        for j in range(4):
            list_merge.append(atlas[j][i])  # 列转置为行
            list_merge = merge(list_merge)
        for k in range(4):
            atlas[k][i] = list_merge[k]  # 行再转置为列
    # return atlas


def move_left(atlas):
    """左移"""
    list_new = []
    for i in atlas:
        list_new.append(merge(i))
    # return list_new


def move_down(atlas):
    """下移"""
    for i in range(4):
        list_new = []
        for j in range(4):
            list_new.append(atlas[-j - 1][i])
        list_new = merge(list_new)
        for k in range(4):
            atlas[k][i] = list_new[-k - 1]
    # return atlas


def move_right(atlas):
    """右移"""
    for i in range(4):
        list_new = []
        for j in range(-1, -5, -1):
            list_new.append(atlas[i][j])
        list_new = merge(list_new)
        for k in range(4):
            atlas[i][k] = list_new[-k - 1]
    # return atlas


def get_0_xy(atlas):
    """得到0元素的坐标"""
    list_xy_0 = []
    for i in range(4):
        for j in range(4):
            if atlas[i][j] == 0:
                list_xy_0.append([i, j])
    return list_xy_0


def creat_number(atlas):
    """在0元素的位置上创建随机数"""
    list_xy_0 = get_0_xy(atlas)
    xy = random.randint(0, len(list_xy_0) - 1)
    atlas[list_xy_0[xy][0]][list_xy_0[xy][1]] = weight_randon()
    return atlas


def weight_randon():
    """以9:1的几率创建2或4元素"""
    number = 4 if random.randint(1, 10) <= 1 else 2
    return number


def defeat(atlas):
    """判断棋盘是否被非0元素填满"""
    state = False
    if len(get_0_xy(atlas)) == 0:
        state = True
    return state


def win(atlas):
    """元素最大值为2048时胜利"""
    for i in range(4):
        for j in range(4):
            if atlas[i][j] == 2048:
                return True


# 游戏初始化
list_atlas = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]
              ]
creat_number(list_atlas)
creat_number(list_atlas)
state_1 = state_2 = True
atlas(list_atlas)
# 进入操作循环
while True:
    list_copy = copy.deepcopy(list_atlas)  # 浅拷贝无法拷贝第二层列表
    try:
        action = input('下一步: ')
    except Exception:
        print('结束游戏')
        break
    if action == 'a' or action == 'd':  # 水平移动情况
        if action == 'a':
            move_left(list_atlas)
        if action == 'd':
            move_right(list_atlas)
        state_1 = defeat(list_atlas)  # 当水平移动后被非0元素填满判断水平失败
    elif action == 'w' or action == 's':  # 垂直移动情况
        if action == 'w':
            move_up(list_atlas)
        if action == 's':
            move_down(list_atlas)
    else:
        continue

    if state_1 and state_2:  # 当水平与垂直同时失败 判定为游戏失败
        print('defeat')
        break
    if win(list_atlas):  # 胜利条件
        atlas(list_atlas)
        print('win')
        break
    if list_copy != list_atlas:  # 当移动后列表产生变化，创建随机数
        creat_number(list_atlas)
    atlas(list_atlas)