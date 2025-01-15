class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n,m=len(matrix),len(matrix[0])
        if m==1:
            return sum(matrix[0])
        la=[matrix[0][:]]+[[0]*m for _ in range(n-1)]
        for i in range(1,n):
            la[i][0]=min(la[i-1][0],la[i-1][1])+matrix[i][0]
            la[i][-1]=min(la[i-1][-1],la[i-1][-2])+matrix[i][-1]
            for j in range(1,m-1):
                la[i][j]=min(la[i-1][j],la[i-1][j-1],la[i-1][j+1])+matrix[i][j]
        return min(la[-1])
#为了省时间和空间，可以在原矩阵的基础上进行修改，而且是方阵，不必要用n,m两个参数。
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        length = len(matrix)
        if length == 1:
            return matrix[0][0]
        for row in range(1, length):
            matrix[row][0] += min(matrix[row-1][0], matrix[row-1][1])
            matrix[row][-1] += min(matrix[row-1][-1], matrix[row-1][-2])
            for col in range(1, length - 1):
                matrix[row][col] += min(matrix[row-1][col], matrix[row-1][col-1], matrix[row-1][col+1])
        return min(matrix[-1])