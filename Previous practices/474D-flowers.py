t,k=map(int,input().split())
from functools import lru_cache
@lru_cache(maxsize=None)
def solve(n):
    if n<k:
        return 1
    return (solve(n-1)+solve(n-k))%(10**9+7)
for _ in range(t):
    a,b=map(int,input().split())
    ans=0
    for i in range(a,b+1):
        ans+=solve(i)
        ans=ans%(10**9+7)
    print(ans)
#用函数递归好像会爆，换DP：
t,k=map(int,input().split())
l=[0]*(10**5+1)
for i in range(k):
    l[i]=1
for i in range(k,10**5+1):
    l[i]=(l[i-1]+l[i-k])%(10**9+7)
for _ in range(t):
    a,b=map(int,input().split())
    print(sum(l[a:b+1]))
#每次sum太慢了，储存和：
t,k=map(int,input().split())
l=[0]*(10**5+1)
s=[0]*(10**5+1)
l[0]=1
for i in range(1,k):
    l[i]=1
    s[i]=(s[i-1]+l[i])%(10**9+7)
for i in range(k,10**5+1):
    l[i]=(l[i-1]+l[i-k])%(10**9+7)
    s[i]=(s[i-1]+l[i])%(10**9+7)
for _ in range(t):
    a,b=map(int,input().split())
    print((s[b]-s[a-1])%(10**9+7))
