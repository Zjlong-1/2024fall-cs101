class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
        def can(i,j):
            while i<j :
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        def solve(i,l):
            if i==n:
                ans.append(l)
                return
            for j in range(i,n):
                if can(i,j):
                    solve(j+1,l+[s[i:j+1]])
        for i in range(n):
            if can(0,i):
                solve(i+1,[s[0:i+1]])
        return ans
#还可以DP：
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[[]]]
        # dp[i]表示s[:i]所有可能的分割方案
        for i in range(1, len(s) + 1):
            dp.append([])
            for j in range(i):
                tmp = s[j:i]
                if tmp == tmp[::-1]:
                    dp[-1].extend(l + [tmp] for l in dp[j])
        return dp[-1]