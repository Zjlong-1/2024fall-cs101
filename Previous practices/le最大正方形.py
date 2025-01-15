class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        la=[[0]*m for _ in range(n)]
        ans=0
        for i in range(m):
            if matrix[0][i]=='1':
                la[0][i]=1
                ans=1
        for i in range(1,n):
            if matrix[i][0]=='1':
                la[i][0]=1
                ans=max(ans,la[i][0])
            for j in range(1,m):
                if matrix[i][j]=='1':
                    la[i][j]=min(la[i-1][j],la[i-1][j-1],la[i][j-1])+1
                    ans=max(ans,la[i][j])
        return ans**2
#确定右下角，取周围三个最小+1