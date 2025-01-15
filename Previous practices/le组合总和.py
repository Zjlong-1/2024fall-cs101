class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(candidates)
        def solve(k,i,l):
            if k==target:
                ans.append(l)
            if i>=n:
                return
            t=0
            while k<=target:
                solve(k+t*candidates[i],i+1,l+[candidates[i]]*t)
                t+=1
        solve(0,0,[])
        return ans
#区别在于是否剪枝，一个超时，一个击败99%
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        n=len(candidates)
        def solve(target,start,l):
            if target==0:
                ans.append(l[:])
                return
            for i in range(start,n):
                if target<candidates[i]:
                    break
                solve(target-candidates[i],i,l+[candidates[i]])
        solve(target,0,[])
        return ans 