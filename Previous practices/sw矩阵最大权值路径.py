n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
ans=-float('inf')
ansl=[]
visit=[[False]*m for _ in range(n)]
l1=[(0,1),(0,-1),(1,0),(-1,0)]
def dfs(x,y,sum,way):
    global ans,ansl
    if x==n-1 and y==m-1:
        if ans<sum:
            ans=sum
            ansl=way[:]
    for dx,dy in l1:
        nx,ny=dx+x,dy+y
        if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
            visit[nx][ny]=True
            dfs(nx,ny,sum+l[nx][ny],way+[(nx+1,ny+1)])
            visit[nx][ny]=False
visit[0][0]=True
dfs(0,0,0,[(1,1)])
for i,j in ansl:
    print(i,j)


import heapq
n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
la=[[float('inf')]*m for _ in range(n)]
heap=[]
di=[(0,1),(0,-1),(1,0),(-1,0)]
la[0][0]=-l[0][0]
prev = [[None] * m for _ in range(n)]
def solve():
    heapq.heappush(heap,(la[0][0],0,0))
    while heap:
        d,x,y=heapq.heappop(heap)
        if x==n-1 and y==m-1:
            path=[]
            while (x, y) != (0, 0):
                path.append((x+1, y+1))
                x, y = prev[x][y]
            path.append((1, 1))
            path.reverse()
            return path
        for dx,dy in di:
            nx,ny=dx+x,dy+y
            if 0<=nx<n and 0<=ny<m and d-l[nx][ny]<la[nx][ny]:
                la[nx][ny]=d-l[nx][ny]
                prev[nx][ny] = (x, y)
                heapq.heappush(heap,(la[nx][ny],nx,ny))
for (i,j) in solve():
    print(i,j)
#超时了。好像也不太好