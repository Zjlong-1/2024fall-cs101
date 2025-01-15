class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        if nums[0]==0:
            return False
        for i in range(n-1):
            if nums[i]==0:
                for k in range(i):
                    if nums[k]<=i-k:
                        return False
        if nums[-1]==0:
            for k in range(n-1):
                if nums[k]>=n-1-k:
                    return True
            return False
        else:
            return True
#一直缝缝补补，但还是错的，原因在于算法有漏洞：
#要用贪心来实时维护最远的距离，我太蠢了，这和我刚刚AC的划分字母区间是一模一样的，中午太晕了，脑子没转过来：
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        k=0
        end=0
        if n==1:
            return True
        while k<n:
            end=max(end,k+nums[k])
            if k==n-1:
                return True
            if end==k and nums[k]==0:
                return False
            k+=1
#记录走到的地方与最远可以到达的地方
#还有另外一种表达方式：（判断最远是否大于终点，会快一点点），也可以省一些分类讨论
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False
