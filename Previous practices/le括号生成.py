class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def solve(l,left,right):
            if left==right==n:
                ans.append(l[:])
                return
            if left==right:
                solve(l+'(',left+1,right)
            elif left>right:
                if left<n:
                    solve(l+'(',left+1,right)
                    solve(l+')',left,right+1)
                else:
                    solve(l+')',left,right+1)
        solve('',0,0)
        return ans
    #及时做剪枝