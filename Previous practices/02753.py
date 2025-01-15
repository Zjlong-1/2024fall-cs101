def f(m):
    if m<=2:
        return 1
    else:
        a=b=1
        for i in range(m-2):
            b=a+b
            a=max(a,b-a)
        return b
n=int(input())
for i in range(n):
    m=int(input())
    print(f(m))