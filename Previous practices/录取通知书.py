from collections import defaultdict
n,m,k=map(int,input().split())
di=defaultdict(int)
ans=defaultdict(int)
for _ in range(n):
    a,b=map(int,input().split())
    di[a]=b
l=[tuple(map(int,input().split())) for _ in range(m)]
l.sort(key=lambda x:(x[1],x[2],x[3],x[4]),reverse=True)
for j in l:
    t=False
    for i in range(-3,0):
        if j[i]!=-1 and di[j[i]]:
            di[j[i]]-=1
            ans[j[0]]=j[i]
            t=True
            break
    if not t:
        ans[j[0]]=-1
l1=list(map(int,input().split()))
ans1=[]
for i in l1:
    ans1.append(ans[i])
print(*ans1)