#pylint:skip-file
from collections import deque
n=int(input())
l=[input() for _ in range(n)]
la=[[False]*n for _ in range(n)]
di=[(0,1),(0,-1),(1,0),(-1,0)]
f=[]
import sys
sys.setrecursionlimit(200000)
def dfs(x,y):
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and  not la[nx][ny] and l[nx][ny]=='1':
            la[nx][ny]=True
            f.append((nx,ny))
            dfs(nx,ny)
def solve():
    for i in range(n):
        for j in range(n):
            if l[i][j]=='1':
                f.append((i,j))
                la[i][j]=True
                dfs(i,j)
                return
solve()
def bfs(x,y):
    q=deque()
    q.append((0,x,y))
    inq=set()
    while q:
        step,x,y=q.popleft()
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not la[nx][ny] and (nx,ny) not in inq:
                if l[nx][ny] == '1':
                    return step+1
                else:
                    inq.add((nx,ny))
                    q.append((step+1,nx,ny))
    return float('inf')
ans=float('inf')
for i,j in f:
    ans=min(ans,bfs(i,j))
print(ans-1)
#每一个点都bfs显然会超时，还有就是bfs最后为了保险在最后都要返回一个return float('inf')
#多个点的bfs要考虑图论中的超级源点，一层一层扩散：
#而且可以在原图上面更改，减小空间复杂度。
from collections import deque
n=int(input())
l=[list(input())for _ in range(n)]
la=[[False]*n for _ in range(n)]
di=[(0,1),(0,-1),(1,0),(-1,0)]
f=deque()
def dfs(x,y):
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and  l[nx][ny]=='1':
            l[nx][ny]=2
            f.append((nx,ny))
            dfs(nx,ny)
def solve():
    for i in range(n):
        for j in range(n):
            if l[i][j]=='1':
                f.append((i,j))
                l[i][j]=2
                dfs(i,j)
                return
solve()
def bfs():
    ans=0
    while f:
        for _ in range(len(f)):
            x,y=f.popleft()
            for dx, dy in di:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n :
                    if l[nx][ny] == '1':
                        return ans
                    elif l[nx][ny]=='0':
                        l[nx][ny]=2
                        f.append((nx,ny))
        ans+=1
print(bfs())
