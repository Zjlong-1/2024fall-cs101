import math
while True:
    n=int(input())
    if n==0:
        break
    l=[]
    for i in range(n):
        t=0
        a,b=map(int,input().split())
        if b>=0:
            t=b+math.ceil(16200/a)
            l.append(t)
    print(min(l))

