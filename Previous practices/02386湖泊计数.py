n,m=map(int,input().split())
l=['.'*(m+2)]+['.'+input()+'.' for i in range(n)]+['.'*(m+2)]
visit=[[False]*(m+2) for _ in range(n+2)]
l1=[(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,1),(-1,0),(1,-1)]
def dfs(x,y):
    visit[x][y] = True
    for nx ,ny in l1:
        if l[x+nx][y+ny]=='W' and not visit[x+nx][y+ny]:
            dfs(x+nx,y+ny)
ans=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if l[i][j]=='W' and not visit[i][j]:
            ans+=1
            dfs(i,j)
print(ans)
#莫名其妙runtime error.不加边了。
n,m=map(int,input().split())
l=[input() for i in range(n)]
l1=[(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,1),(-1,0),(1,-1)]
visit=[[False]*m for _ in range(n)]
def dfs(x,y):
    visit[x][y] = True
    for nx ,ny in l1:
        x1,y1=nx+x,ny+y
        if 0<=x1<n and 0<=y1<n and l[x1][y1]=='W' and not visit[x1][y1]:
            dfs(x1,y1)
ans=0
for i in range(n):
    for j in range(m):
        if l[i][j]=='W' and not visit[i][j]:
            ans+=1
            dfs(i,j)
print(ans)
#其实都是对的，只是递归深度超了：用sys来重设。
import sys
sys.setrecursionlimit(20000)
n,m=map(int,input().split())
l=[list(input()) for i in range(n)]
l1=[(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,1),(-1,0),(1,-1)]
def dfs(x,y):
    l[x][y]='.'
    for nx ,ny in l1:
        x1,y1=nx+x,ny+y
        if 0<=x1<n and 0<=y1<m and l[x1][y1]=='W' :
            dfs(x1,y1)
ans=0
for i in range(n):
    for j in range(m):
        if l[i][j]=='W' :
            ans+=1
            dfs(i,j)
print(ans)