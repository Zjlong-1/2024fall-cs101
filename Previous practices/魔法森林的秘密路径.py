from functools import lru_cache
m,n=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
la=[]
d=[(0,1),(0,-1),(1,0),(-1,0)]
def can(x,y):
    for dx,dy in d:
        nx,ny=dx+x,dy+y
        if 0<=nx<m and 0<=ny<n and l[nx][ny]>=l[x][y]:
            return False
    return True
for i in range(m):
    for j in range(n):
        if can(i,j):
            la.append((i,j))
visit=[[False]*n for _ in range(m)]
@lru_cache(maxsize=None)
def dfs(x,y,step):
    cnt=step
    for dx,dy in d:
        nx,ny=dx+x,dy+y
        if 0<=nx<m and 0<=ny<n and l[nx][ny]<l[x][y]:
            visit[nx][ny]=True
            cnt=max(cnt,dfs(nx,ny,step+1))
            visit[nx][ny] = False
    return cnt
ans=0
for x,y in la:
    visit[x][y]=True
    ans=max(dfs(x,y,1),ans)
    visit[x][y]=False
print(ans)