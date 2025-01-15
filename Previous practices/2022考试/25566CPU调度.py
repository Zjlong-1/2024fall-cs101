n=int(input())
l=[]
t=0
for _ in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
    t+=a
l.sort(key=lambda x:(-x[1],x[0]))
ans=t
for i in range(n):
    t-=l[i][0]
    if t<l[i][1]:
        ans+=l[i][1]-t
        t=l[i][1]
print(ans)