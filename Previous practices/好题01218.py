n=int(input())
for i in range(n):
    t=int(input())
    print(int(t**0.5))

#计算机语言来确定因子
for _ in range(int(input())):
    n = int(input())
    lst = [0] * n

    for j in range(2, n + 1):
        for i in range(j - 1, n, j):
            lst[i]^= 1

    print(lst.count(0))