#感觉要双指针，做最便宜的，卖最贵的
p=int(input())
l=list(map(int,input().split()))
l.sort()
n=len(l)
i=0
j=n-1
ans=0
while True:
    while i<n and p >= l[i]:
        p -= l[i]
        i += 1
        ans+=1
    if  ans>=1 and j>i :
        p+=l[j]-l[i]
        j-=1
        i+=1
    else:
        break
print(ans)
