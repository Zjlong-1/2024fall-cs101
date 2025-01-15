from functools import lru_cache
@lru_cache(maxsize=None)
def solve(m,n,maxsize):
    ans=0
    if n==1 :
        if m<=maxsize:
            return 1
        return 0
    if m==0:
        return 1
    for i in range(min(maxsize,m),0,-1):
        ans+=solve(m-i,n-1,i)
    return ans
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    print(solve(m,n,m))