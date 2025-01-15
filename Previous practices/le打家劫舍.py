#用前i个的DP果然快很多：
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        la=[0]*n
        la[0]=nums[0]
        if n==1:
            return nums[0]
        la[1]=max(nums[1],nums[0])
        for i in range(2,n):
            la[i]=max(la[i-1],la[i-2]+nums[i])
        return la[-1]