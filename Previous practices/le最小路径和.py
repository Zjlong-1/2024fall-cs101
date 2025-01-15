class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        la=[[0]*m for _ in range(n)]
        la[0][0]=grid[0][0]
        for i in range(1,m):
            la[0][i]=la[0][i-1]+grid[0][i]
        for j in range(1,n):
            la[j][0]=la[j-1][0]+grid[j][0]
        for i in range(1,n):
            for j in range(1,m):
                la[i][j]=min(la[i-1][j],la[i][j-1])+grid[i][j]
        return la[-1][-1]
#有一个小优化：将第3个循环套在第2个里面。
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + grid[i][j]
        m = len(grid)
        n = len(grid[0])
        cur = grid[0] # cur =[1, 3, 1]
        for i in range(1,n):
            cur[i] +=cur[i-1]
        for i in range(1,m):
            cur[0] +=grid[i][0]
            for j in range(1, n):
                cur[j] = min(cur[j-1], cur[j]) + grid[i][j]
        return cur[n-1]