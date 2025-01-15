n,m=map(int,input().split())
la=[[0]*m for _ in range(n)]
l=[[0]*(m+2) ]
for i in range(n):
    k=[0]
    k+=list(map(int,input().split()))
    k.append(0)
    l.append(k)
l.append([0]*(m+2))
for i in range(1,n+1):
    for j in range(1,m+1):
        t=l[i+1][j]+l[i-1][j]+l[i][j+1]+l[i][j-1]+l[i+1][j+1]+l[i-1][j-1]+l[i-1][j+1]+l[i+1][j-1]
        if l[i][j]==1:
            if  t==2 or t==3:
                la[i-1][j-1]=1
        if l[i][j]==0:
            if t==3:
                la[i-1][j-1]=1
for i in range(n):
    print(*la[i])


