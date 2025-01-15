from bisect import bisect_right
n=int(input())
l=list(map(int,input().split()))
la=[float('inf')]*n
for i in range(n):
    k=bisect_right(la,l[i])
    la[k]=l[i]
def solve():
    for i in range(n):
        if la[i]==float('inf'):
            print(i)
            return
    print(n)
    return
solve()
#好吧，还是刻板印象，又看错题了。要分为两半，一半单调增一般单调减少
#还是有一点问题，因为中间结尾的点确定了，所以二分法不行了，直接用DP+贪心
#还有条件！！！不连续
n=int(input())
l=list(map(int,input().split()))
la1=[1]*n
la2=la1[:]
for i in range(1,n):
    for j in range(i):
        if l[j]<l[i]:
            la1[i]=max(la1[i],la1[j]+1)
for i in range(n-2,-1,-1):
    for j in range(n-1,i,-1):
        if l[i]>l[j]:
            la2[i] = max(la2[i], la2[j] + 1)
ans=max(la1)
for i in range(n-1):
    for j in range(i+1,n):
        if l[i]>l[j]:
            ans=max(ans,la1[i]+la2[j])
print(ans)
#跟我考试题的思路一样