import math

def lama_method():
    re = 0
    n = 1
    while n <= 100000:
        print('第%d轮'%n)
        re += 1 / (n*n)
        n += 1
    return math.sqrt(re*6)


if __name__ == '__main__':
    print(lama_method())