class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        inq=set()
        q=deque()
        n=len(grid)
        inq.add((0,0,0,1))
        q.append((0,0,0,0,1))
        d1=[(0,1,0,1),(1,0,1,0)]
        d2=[(0,1,0,1),(1,0,1,0),(0,0,-1,1)]
        d3=[(0,1,0,1),(1,0,1,0),(0,0,1,-1)]
        d=defaultdict(list)
        while q :
            step,x1,y1,x2,y2=q.popleft()
            if x1==x2==y2==n-1 and y1==n-2:
                return step
            if x1==x2 and x1<n-1 and  grid[x1+1][y1]==grid[x2+1][y2]==0:
                for dx1,dy1,dx2,dy2 in d3:
                    nx1,ny1,nx2,ny2=dx1+x1,dy1+y1,dx2+x2,dy2+y2
                    if 0<= nx1<n and 0<=nx2<n and 0<=ny1<n and 0<=ny2<n and grid[nx1][ny1]==grid[nx2][ny2]==0 and (nx1,ny1,nx2,ny2) not in inq:
                        inq.add((nx1,ny1,nx2,ny2))
                        q.append((step+1,nx1,ny1,nx2,ny2))
            elif y1==y2 and y1<n-1 and grid[x1][y1+1]==grid[x2][y2+1]==0 :
                for dx1,dy1,dx2,dy2 in d2:
                    nx1,ny1,nx2,ny2=dx1+x1,dy1+y1,dx2+x2,dy2+y2
                    if 0<= nx1<n and 0<=nx2<n and 0<=ny1<n and 0<=ny2<n and grid[nx1][ny1]==grid[nx2][ny2]==0 and (nx1,ny1,nx2,ny2) not in inq:
                        inq.add((nx1,ny1,nx2,ny2))
                        q.append((step+1,nx1,ny1,nx2,ny2))
            elif x1==x2:
                dx1,dy1,dx2,dy2 = d1[0]
                nx1,ny1,nx2,ny2=dx1+x1,dy1+y1,dx2+x2,dy2+y2
                if 0<= nx1<n and 0<=nx2<n and 0<=ny1<n and 0<=ny2<n and grid[nx1][ny1]==grid[nx2][ny2]==0 and (nx1,ny1,nx2,ny2) not in inq:
                    inq.add((nx1,ny1,nx2,ny2))
                    q.append((step+1,nx1,ny1,nx2,ny2))
            elif y1==y2:
                dx1,dy1,dx2,dy2 = d1[1]
                nx1,ny1,nx2,ny2=dx1+x1,dy1+y1,dx2+x2,dy2+y2
                if 0<= nx1<n and 0<=nx2<n and 0<=ny1<n and 0<=ny2<n and grid[nx1][ny1]==grid[nx2][ny2]==0 and (nx1,ny1,nx2,ny2) not in inq:
                    inq.add((nx1,ny1,nx2,ny2))
                    q.append((step+1,nx1,ny1,nx2,ny2))
        return -1
#抽象的一堆重复代码
