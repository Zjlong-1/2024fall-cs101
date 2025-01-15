from collections import deque
def f(grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n, m = len(grid), len(grid[0])

    def bfs(x, y):
        q = deque()
        inq = set()
        q.append((0, x, y))
        inq.add((x, y))
        while q:
            step, i, j = q.popleft()
            if grid[i][j] == 2:
                return step
            for dx, dy in directions:
                nx, ny = dx + i, dy + j
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 0 and (nx, ny) not in inq:
                    inq.add((nx, ny))
                    q.append((step + 1, nx, ny))
        return -1

    def solve():
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    k = bfs(i, j)
                    if k == -1:
                        return -1
                    ans = max(ans, k)
        return ans

    return solve()
print(f([[2,1,1],[1,1,1],[0,1,2]]))
#老套的bfs
#leetcode提交代码：
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        n,m=len(grid),len(grid[0])
        def bfs(x,y):
            q=deque()
            inq=set()
            q.append((0,x,y))
            inq.add((x,y))
            while q:
                step,i,j=q.popleft()
                if grid[i][j]==2:
                    return step
                for dx,dy in directions:
                    nx,ny=dx+i,dy+j
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]!=0 and (nx,ny) not in inq:
                        inq.add((nx,ny))
                        q.append((step+1,nx,ny))
            return -1
        def solve():
            ans=0
            for i in range(n):
                for j in range(m):
                    if grid[i][j]==1:
                        k=bfs(i,j)
                        if k==-1:
                            return -1
                        ans=max(ans,k)
            return ans
        return solve()
#优化：超级源点：
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c) -> (int, int):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        if any(1 in row for row in grid):
            return -1
        return d

#最后一步还可以优化：
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    fresh += 1
                elif x == 2:
                    q.append((i, j))

        ans = 0
        while q and fresh:
            ans += 1
            tmp = q
            q = []
            for x, y in tmp:
                for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        fresh -= 1
                        grid[i][j] = 2
                        q.append((i, j))
        return -1 if fresh else ans