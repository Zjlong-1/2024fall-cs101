def f(candidates,target):
    candidates.sort()
    n = len(candidates)
    ans = []

    def solve(target, index, sum1, l):
        s=set()
        for i in range(index, n):
            if candidates[i] in s:
                continue
            s.add(candidates[i])
            k = sum1 + candidates[i]
            if k == target:
                ans.append(l + [candidates[i]])
                return
            elif k < target:
                solve(target, i + 1, k, l + [candidates[i]])
            else:
                return

    solve(target, 0, 0, [])
    return ans
print(f([10,1,2,7,6,1,5],8))
#leetcode提交代码：（去重，即防止某个数多次用，用set放在函数开头）
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n=len(candidates)
        ans=[]
        def solve(target,index,sum1,l):
            s=set()
            for i in range(index,n):
                if candidates[i] in s:
                    continue
                s.add(candidates[i])
                k=sum1+candidates[i]
                if k==target:
                    ans.append(l+[candidates[i]])
                    return
                elif k<target:
                    solve(target,i+1,k,l+[candidates[i]])
        solve(target,0,0,[])
        return ans