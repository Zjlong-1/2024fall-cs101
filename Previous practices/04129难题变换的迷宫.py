from collections import deque
di=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(x,y):
    q=deque()
    inq=set()
    q.append((0,x,y))
    inq.add((0,x,y))
    while q:
        ti,x,y=q.popleft()
        for dx,dy in di:
            nx,ny=dx+x,dy+y
            kt=(ti+1)%k
            if 0<=nx<r and 0<=ny<c and (kt,nx,ny) not in inq:
                if l[nx][ny]=='E':
                    return ti+1
                elif l[nx][ny]!='#' or kt==0:
                    q.append((ti+1,nx,ny))
                    inq.add((kt,nx,ny))
    return 'Oop!'
t=int(input())
for _ in range(t):
    r, c, k = map(int, input().split())
    l = [list(input()) for i in range(r)]
    def solve():
        for i in range(r):
            for j in range(c):
                if l[i][j]=='S':
                    print(bfs(i,j))
                    return
    solve()
