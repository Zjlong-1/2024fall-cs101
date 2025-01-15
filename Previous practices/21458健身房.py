t,n=map(int,input().split())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
la=[0]+[-float('inf')]*t
for a,b in l:
    for j in range(t,a-1,-1):
        la[j]=max(la[j],la[j-a]+b)
if la[t]==-float('inf'):
    print(-1)
else:
    print(la[t])

