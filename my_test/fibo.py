"""
生成斐波那契数列的三种方法
"""


# 方法一：数列推导
def fibo_1(n):
    a, b = 1, 1
    l = []
    while n > 0:
        l.append(a)
        a, b = b, a + b
        n -= 1
    return l


# 方法二： 递归推导
def fibo_2(n):
    if n <= 1:
        return 1
    else:
        return fibo_2(n - 1) + fibo_2(n - 2)  # 返回第n个斐波那契数


# 方法三：生成器
def fibo_3(n):
    a, b = 1, 1
    while n > 0:
        yield a
        a, b = b, a + b
        n -= 1


if __name__ == '__main__':
    res = fibo_1(10)
    print("方法一生成：", res)

    print('方法二生成：', end=' ')
    for i in range(10):
        print(fibo_2(i), end=', ')
    print()

    print('方法三生成：', end=' ')
    for i in fibo_3(10):
        print(i, end=', ')
