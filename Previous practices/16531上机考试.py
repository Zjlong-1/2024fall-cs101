#考虑构造一个一一映射，K*X+B型（B是为了保证空格与全是零区分开）
from collections import defaultdict
m,n=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(m)]
di=[(0,-1),(0,1),(1,0),(-1,0)]
def f():
    k=list(map(int,input().split()))
    t=len(k)
    if t==0:
        return -1,0
    f1=0
    for i in range(t):
        f1+=(10**i)*k[i]
    return f1,sum(k)
s=defaultdict(int)
s1=defaultdict(int)
for j in range(m*n):
    f2,f3=f()
    s[j]=f2
    s1[f3]+=1
def solve(i,j):
    for dx,dy in di:
        nx,ny=dx+i,dy+j
        if 0<=nx<m and 0<=ny<n and s[l[nx][ny]]==s[l[i][j]]:
            return True
    return False
ans=0
for i in range(m):
    for j in range(n):
        if solve(i,j):
            ans+=1
ansl=sorted(s1.items(),reverse=True)
ans1=0
bi=0.4*m*n
for k,t in ansl:
    if ans1+t>bi:
        print(ans,ans1)
        break
    else:
        ans1+=t
#写完这道题感觉功力暴涨，感觉这个映射思路非常好



