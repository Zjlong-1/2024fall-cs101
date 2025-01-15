from collections import deque
m,n=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(m)]
l1=[(1,0),(0,1),(0,-1),(-1,0)]
def bfs(x,y):
    q=deque()
    step=0
    inq=set()
    q.append((step,(x,y)))
    inq.add((x,y))
    while q:
        step,(x,y)=q.popleft()
        if l[x][y]==1:
            return step
        for dx,dy in l1:
            nx,ny=dx+x,dy+y
            if 0<=nx<m and 0<=ny<n and l[nx][ny]!=2 and (nx,ny) not in inq:
                inq.add((nx,ny))
                q.append((step+1,(nx,ny)))
    return 'NO'
print(bfs(0,0))
