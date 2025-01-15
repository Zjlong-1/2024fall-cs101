class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        m=len(nums2)
        la=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if nums1[i-1]==nums2[j-1]:
                    la[i][j]=la[i-1][j-1]+1
                else:
                    la[i][j]=max(la[i-1][j],la[i][j-1])
        return la[-1][-1]
#递归同理：
class Solution:
    def maxUncrossedLines(self, s: List[int], t: List[int]) -> int:
        n, m = len(s), len(t)
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if s[i] == t[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))
        return dfs(n - 1, m - 1)
#还可以用set做剪枝：
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        m = len(nums1)
        n = len(nums2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        maps = dict()
        for i in range(1, m + 1):
            maps[nums1[i - 1]] = i - 1
            for j in range(1, n + 1):
                if nums2[j - 1] not in maps:
                    dp[i][j] = dp[i][j - 1]
                else:
                    index = maps[nums2[j - 1]]
                    dp[i][j] = max(dp[i][j - 1], dp[index][j - 1] + 1)
        # print(dp)
        return dp[-1][-1]