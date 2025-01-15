class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        l=[]
        n=len(nums)
        def z(k,l):
            ans.append(l)
            for j in range(i,n):
                z(j+1,l+[nums[j]])
        z(0,l)
        return ans
            