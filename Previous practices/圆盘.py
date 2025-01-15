n,m=map(int,input().split())
l=[tuple(map(int,input().split())) for _ in range(n)]
la=[float('inf')]*(m+1)
sa=sum(l[i][0] for i in range(n))
la[sa]=0
for i in range(n):
    k=l[i][1]-l[i][0]
    if k>0:
        for j in range(m,-1,-1):
            if la[j]!=float('inf') :
                ns=j+k
                if 0<=ns<m+1:
                    la[ns]=min(la[ns],la[j]+1)
    if k<0:
        for j in range(m+1):
            if la[j]!=float('inf') :
                ns=j+k
                if 0<=ns<m+1:
                    la[ns]=min(la[ns],la[j]+1)
for i in range(m+1):
    if la[i]!=float('inf'):
        print(la[i])
    else:
        print(-1)