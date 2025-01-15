class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        if matrix[0][0]>target or matrix[-1][-1]<target:
            return False
        k=-1
        for i in range(n):
            if matrix[i][-1]>=target:
                k=i
                break
        t=bisect_left(matrix[k],target)
        if matrix[k][t]==target:
            return True
        else:
            return False
#还可以手动二分：
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = -1, m * n
        while left + 1 < right:
            mid = (left + right) // 2
            x = matrix[mid // n][mid % n]
            if x == target:
                return True
            if x < target:
                left = mid
            else:
                right = mid
        return False
