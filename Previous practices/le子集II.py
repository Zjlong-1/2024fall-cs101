class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        def solve(i,l):
            ans.append(l)
            s=set()
            for j in range(i,n):
                if nums[j] not in s:
                    solve(j+1,l+[nums[j]])
                    s.add(nums[j])
        solve(0,[])
        return ans