m,n,p,q=map(int,input().split())
l1=[list(map(int,input().split())) for _ in range(m)]
l2=[list(map(int,input().split())) for _ in range(p)]
la=[[0]*(n+1-q) for _ in range(m+1-p)]
for i in range(m+1-p):
    for j in range(n+1-q):
        la[i][j]=sum(l2[k][g]*l1[k+i][g+j] for k in range(p) for g in range(q))
for i in la:
    print(*i)
