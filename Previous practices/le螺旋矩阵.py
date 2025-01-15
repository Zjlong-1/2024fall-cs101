class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        i,j=0,0
        k=1
        l=[[True]*m for _ in range(n)]
        la=[matrix[i][j]]
        l[0][0]=False
        count=1
        while True:
            if count==m*n:
                break
            if k==1 :
                if j+1<m and l[i][j+1]:
                    j+=1
                    la.append(matrix[i][j])
                    l[i][j]=False
                    count+=1
                else:
                    k=2
            elif k==2:
                if i+1<n and l[i+1][j]:
                    i+=1
                    la.append(matrix[i][j])
                    l[i][j] = False
                    count += 1
                else:
                    k=3
            elif k==3:
                if j-1>=0 and l[i][j-1]:
                    j-=1
                    la.append(matrix[i][j])
                    l[i][j] = False
                    count += 1
                else:
                    k=4
            elif k==4:
                if i-1>=0 and l[i-1][j]:
                    i-=1
                    la.append(matrix[i][j])
                    l[i][j] = False
                    count += 1
                else:
                    k=1
        return la
#用数字记录走的方向，不断判断是否可以按照原方向走下去，如果不行则装90度继续走，有点像古代走迷宫的一个策略，碰到墙就转弯，否则就保持原有方向继续走，看最后是否可以出去。
#同一思路，另一种解法：
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns
        order = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directionIndex = 0
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return order
#也可以多步多步来弄：
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order

