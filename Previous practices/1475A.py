n=int(input())
for i in range(n):
    m=int(input())
    if m==1:
        print('NO')
    elif m%2==1:
        print('YES')
    else:
        while m%2==0:
            m=m/2
        if m==1:
            print('NO')
        else:
            print('YES')
#事实上，我的方法复杂了。只需要去除m中的2的幂即可
t = int(input())
for _ in range(t):
    n = int(input())

    # 不断除以 2 直到 n 是奇数
    while n % 2 == 0:
        n //= 2

    # 检查 n 是否大于 1
    if n > 1:
        print("YES")
    else:
        print("NO")