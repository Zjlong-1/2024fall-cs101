n=int(input())
l=list(map(int,input().split()))
ans=0
while l :
    k=l.pop()
    if k==0:
        continue
    for i in range(len(l)-1,-1,-1):
        if l[i]>=k:
            l[i]-=k
        else:
            break
    ans+=1
print(ans)
