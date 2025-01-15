class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=[]
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    l.append((i,j))
        for i,j in l:
            for k in range(n):
                matrix[k][j]=0
            for k in range(m):
                matrix[i][k]=0