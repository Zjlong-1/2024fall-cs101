n=int(input())
l=list(map(int,input().split()))
la1=[1]*n
la2=la1[:]
for i in range(1,n):
    if l[i]>l[i-1]:
        la1[i]=la1[i-1]+1
for i in range(n-2,-1,-1):
    if l[i]>l[i+1]:
        la2[i]=la2[i+1]+1
ans=0
for i in range(n):
    ans+=max(la1[i],la2[i])
print(ans)

