class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        la=[[-1]*m for _ in range(n)]
        di=[(0,1),(0,-1),(-1,0),(1,0)]
        def solve(i,j):
            q=deque()
            inq=set()
            q.append((0,i,j))
            inq.add((i,j))
            while q:
                step,x,y=q.popleft()
                if mat[x][y]==0:
                    return step
                for dx,dy in di:
                    nx,ny=dx+x,dy+y
                    if 0<=nx<n and m>ny>=0 and (nx,ny) not in inq:
                        inq.add((nx,ny))
                        q.append((step+1,nx,ny))
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    la[i][j]=0
                else:
                    la[i][j]=solve(i,j)
        return la
#一个比较妙的图论做法：（像水波一样，层层扩散）
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)

        # 广度优先搜索
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        return dist
#DP两个方向：
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        if not m:
            return []
        n = len(mat[0])
        dp = [[m * n + 2] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if i - 1 >= 0:
                        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j])
                    if j - 1 >= 0:
                        dp[i][j] = min(dp[i][j - 1] + 1, dp[i][j])
                else:
                    dp[i][j] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 1:
                    if i + 1 < m:
                        dp[i][j] = min(dp[i + 1][j] + 1, dp[i][j])
                    if j + 1 < n:
                        dp[i][j] = min(dp[i][j + 1] + 1, dp[i][j])
                else:
                    dp[i][j] = 0
        return dp

