class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        from bisect import bisect_right
        nums.sort()
        k=bisect_right(nums,0)
        if k==len(nums):
            return 1
        if nums[k]>1:
            return 1
        ans=nums[-1]+1
        for i in range(k+1,len(nums)):
            if nums[i]-nums[i-1]>1:
                return nums[i-1]+1
        return ans
#一种比较绕的方法：
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
