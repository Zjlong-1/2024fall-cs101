n,m=map(int,input().split())
l=[0]
l+=list(map(int,input().split()))
l.append(m)
if n%2==0:
    t=n//2+1
    la=[0]*t
    max1=0
    w=0
    for i in range(t):
        la[i]+=l[i*2+1]-l[i*2]
         if max1<la[i]:
             w=i
             max1=la[i]
#为了省一点点时间导致空间利用极大，而且十分难算（整体无法考虑是否可以插入），不如直接枚举。
#用2来做跨度可以避免分奇偶讨论
n,m=map(int,input().split())
l=[0]
l+=list(map(int,input().split()))
l.append(m)
t=0
s=0
for i in range(1,n+2,2):
    t+=l[i]-l[i-1]
ans=t
for i in range(2,n+2,2):
    s+=l[i-1]-l[i-2]
    if l[i]>l[i-1]+1:
        k=t-s
        ans=max(ans,s+m-l[i-1]-k-1)
print(ans)



