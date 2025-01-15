n,k=map(int,input().split())
if n**2<k:
    print(-1)
elif k>=1:
    l=[[0]*n for _ in range(n)]
    for i in range(n):
        if k==0:
            break
        l[i][i]=1
        k-=1
        t = i + 1
        while k>=2:
            if t==n:
                break
            l[i][t]=1
            l[t][i]=1
            t+=1
            k -= 2
    for i in range(n):
        print(*l[i])
else:
    l=[0]*n
    for i in range(n):
        print(*l)
#细节题，一步一步缓慢剥开。




