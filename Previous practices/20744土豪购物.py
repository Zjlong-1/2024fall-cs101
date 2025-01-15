l=list(map(int,input().split(',')))
n=len(l)
def solve():
    k=max(l)
    if k<0:
        return k
    la1=[-float('inf')]*n
    la2=la1[:]
    la1[0]=l[0]#jiewei
    la2[-1] = l[-1]
    for i in range(1,n):
        la1[i]=max(la1[i-1]+l[i],l[i])
        la2[n-i-1]=max(la2[n-i]+l[n-i-1],l[n-i-1])
    ans=max(la1)
    for i in range(1,n-1):
        ans=max(ans,la1[i-1]+la2[i+1])
    return ans
print(solve())
#思路：也是分两种情况，一种是拿出一个，另一种是不拿。事实上只要考虑两次贪心，
#以第i个结尾的最大和，和以第i个开头的最大和。形成拼接
#也可以两步DP：
a = list(map(int, input().split(',')))
dp1 = [0] * len(a);
dp2 = [0] * len(a)
dp1[0] = a[0];
dp2[0] = a[0]
for i in range(1, len(a)):
    dp1[i] = max(dp1[i - 1] + a[i], a[i])
    dp2[i] = max(dp1[i - 1], dp2[i - 1] + a[i], a[i])
print(max(dp2))



