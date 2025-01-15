class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        la=[[0]*m for _ in range(n)]
        if obstacleGrid[0][0]==1:
            return 0
        la[0][0]=1
        for i in range(1,m):
            if obstacleGrid[0][i]!=1:
                la[0][i]=la[0][i-1]
        for i in range(1,n):
            if obstacleGrid[i][0]!=1 :
                la[i][0]=la[i-1][0]
            for j in range(1,m):
                if obstacleGrid[i][j]!=1:
                    la[i][j]=la[i][j-1]+la[i-1][j]
        return la[-1][-1]