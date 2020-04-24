"""
牛顿法开平方根
"""
def my_sqrt(a):
    x = a
    y = 0.0
    while(abs(x - y) > 0.000000000001):
        y = x
        x = 0.5 * (x + a / x)
    return print(x)


if __name__ == '__main__':
    while True:
        try:
            num = int(input('num = '))
            break
        except ValueError:
            print('输入数值')
    my_sqrt(num)
