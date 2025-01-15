from collections import deque
m,n,p=map(int,input().split())
l=[input().split() for _ in range(m)]
di=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(x1,y1,x2,y2):
    ans=float('inf')
    q=deque()
    inq=set()
    q.append((0,x1,y1))
    inq.add((x1,y1))
    while q:
        step,x,y=q.popleft()
        if x==x2 and y==y2:
            ans=min(step,ans)
        for dx,dy in di:
            nx,ny=dx+x,dy+y
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in inq  and l[nx][ny]!='#':
                step1=(step+abs(int(l[nx][ny])-int(l[x][y])))
                inq.add((step1,nx,ny))
                q.append((step1,nx,ny))
    return ans
for i in range(p):
    x1, y1, x2, y2=map(int,input().split())
    k=bfs(x1,y1,x2,y2)
    if k==float('inf'):
        print('NO')
    else:
        print(k)
#bfs不适合找所有的路径，要dfs或者优化。
#dijkstra
import heapq
m,n,p=map(int,input().split())
l=[input().split() for _ in range(m)]
di=[(0,1),(0,-1),(1,0),(-1,0)]
def solve(x1,y1,x2,y2):
    heap=[]
    la=[[float('inf')]*n for _ in range(m)]
    if l[x1][y1]=='#' or l[x2][y2]=='#':
        return 'NO'
    la[x1][y1]=0
    heapq.heappush(heap,(0,x1,y1))
    while heap:
        d,x,y=heapq.heappop(heap)
        if x==x2 and y==y2:
            return d
        k=int(l[x][y])
        for dx,dy in di:
            nx,ny=dx+x,dy+y
            if 0<=nx<m and 0<=ny<n and l[nx][ny]!='#':
                if la[nx][ny]>d+abs(k-int(l[nx][ny])):
                    la[nx][ny]=d+abs(k-int(l[nx][ny]))
                    heapq.heappush(heap,(la[nx][ny],nx,ny))
    return 'NO'
for _ in range(p):
    x1, y1, x2, y2=map(int,input().split())
    print(solve(x1,y1,x2,y2))





