#有一点dp的思想，实际上考虑的是确定结尾的最短子序列
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        n=len(nums)
        ans=n+1
        s,e=0,0
        k=0
        while e<n:
            k += nums[e]
            while k>=target:
                ans=min(ans,e-s+1)
                k-=nums[s]
                s+=1
            e+=1
        return 0 if ans==n+1 else ans
