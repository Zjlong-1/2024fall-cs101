while True:
    try:
        n, m = map(int, input().split())
        a = 0
        while True:
            if n == m:
                a = n
                break
            elif n > m:
                if n % m == 0:
                    a = m
                    break
                else:
                    n = n % m
            else:
                if m % n == 0:
                    a = n
                    break
                else:
                    m = m % n
        print(a)
    except EOFError:
        break
#基于高中所学的欧拉递降法得出的解法
#也可以偷懒直接用内置函数：
from math import gcd

while True:
    try:
        a, b = input().split()
        print(gcd(int(a), int(b)))
    except EOFError:
        break
#也可以用比较蠢的算法来确定最大公约数：
# 求两个整数的最大公约数
def comfac(a, b):
    n = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            n = i
    return n

while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(comfac(a, b))


