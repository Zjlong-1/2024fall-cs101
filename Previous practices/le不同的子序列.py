class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #s的前j个中出现t前i个的次数
        n,m=len(s),len(t)
        la=[[0]*n for _ in range(m)]
        if s[0]==t[0]:
            la[0][0]=1
        for i in range(1,n):
            if s[i]==t[0]:
                la[0][i]=la[0][i-1]+1
            else:la[0][i]=la[0][i-1]
        for i in range(1,m):
            for j in range(i,n):
                if t[i]==s[j]:
                    la[i][j]+=la[i-1][j-1]+la[i][j-1]
                else:
                    la[i][j]=la[i][j-1]
        return la[-1][-1]
#递归好像快很多（加缓存）因为向左弄(s[:j]和t[:i]（与我的DP相比反向）)剪枝的程度更大：
#记 dfs(i, j) 表示匹配到字符 s[i] 和 t[j] 时的方案数目，当递归搜索到达 s[i] 时我们有两种选择
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1, n2 = len(s), len(t)

        @cache
        def dfs(i, j):
            if j == n2:
                return 1
            if n1 - i < n2 - j:
                return 0

            return sum(
                [dfs(i + 1, j + 1) if s[i] == t[j] else 0,
                 dfs(i + 1, j)]
            )

        return dfs(0, 0)