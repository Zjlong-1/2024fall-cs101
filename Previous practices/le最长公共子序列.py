class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def solve(x,y):
            if x<0 or y<0:
                return 0
            if text1[x]==text2[y]:
                return solve(x-1,y-1)+1
            return max(solve(x,y-1),solve(x-1,y))
        return solve(len(text1)-1,len(text2)-1)
#但超时了,没加@lru_cache(maxsize=None)!!!!，加上就可以过了。
#但DP这次快一点，因为递归没有省计算，反而还要储存数据导致时间变慢
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]
#有一点玄的代码：
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        import bisect
        # 初始化dic，记录text1中所有出现过的字符 {text1[i]: [],...}
        dic = {}
        for c in text1:
            if not c in dic:
                dic[c] = []
        # 将text2中存在于text1中的字符的索引添加到dic中去（从大到小）
        for i in range(len(text2)):
            if (c := text2[i]) in dic:
                dic[c].insert(0, i)
        # arr记录各text1与text2共同出现的字符的索引（降序）
        arr = []
        for c in text1:
            arr.extend(dic[c])
        # 此时，问题即为俄罗斯信封套娃问题，前面的操作相当于重新排序
        d = []  # d[i] 以 i+1 长的最长递增子元素末尾元素的最小值
        for i in arr:
            index = bisect.bisect_left(d, i)
            if index == len(d):
                d.append(i)
            else:
                d[index] = i
        return len(d)