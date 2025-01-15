class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        s=sum(nums)
        if s%2==1:
            return False
        s=s//2
        la=[False]*(s+1)
        la[0]=True
        nums.sort()
        for i in range(n):
            k=nums[i]
            for j in range(s,k-1,-1):
                if la[j-k]:
                    la[j]=True
        return  la[-1]