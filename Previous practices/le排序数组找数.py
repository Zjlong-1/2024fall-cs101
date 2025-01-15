class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        if n==0:
            return [-1,-1]
        k=bisect_left(nums,target)
        m=bisect_right(nums,target)
        left,right=-1,-1
        if k==n:
            return [-1,-1]
        if nums[k]==target:
            left=k
            right=m-1
        return [left,right]