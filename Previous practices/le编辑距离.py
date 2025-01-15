class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1,word2=word2,word1
        n,m=len(word1),len(word2)
        if n==0:
            return m
        if m==0:
            return n
        la=[[max(m,n)]*m for _ in range(n)]
        s=set(word1[0])
        s1=set()
        for i in range(m):
            s1.add(word2[i])
            if word1[0] in s1:
                la[0][i]=i
            else:la[0][i]=i+1
        for i in range(1,n):
            s.add(word1[i])
            if word2[0] in s:
                la[i][0]=i
            else:
                la[i][0]=i+1
            for j in range(1,m):
                if word1[i]==word2[j]:
                    la[i][j]=la[i-1][j-1]
                else:
                    la[i][j]=min(la[i-1][j],la[i][j-1],la[i-1][j-1])+1
        return la[-1][-1]
#又是动态规划，还可以递归加记忆化：（可以省一些时间，不需要全部弄出来）
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = [[-1] * n for _ in range(m)]

        def dp(word1, i, word2, j):
            # base case
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1

            if memo[i][j] != -1:
                return memo[i][j]

            if word1[i] == word2[j]:
                memo[i][j] = dp(word1, i - 1, word2, j - 1)
                return memo[i][j]
            else:
                memo[i][j] = min(
                    dp(word1, i - 1, word2, j) + 1,  # 删除, i 向前移动一位
                    dp(word1, i, word2, j - 1) + 1,  # 插入, i 不动, j 与新插入的字符相同, j 向前移动一位
                    dp(word1, i - 1, word1, j - 1) + 1,  # 替换, 共同前移一位
                )
                return memo[i][j]

        return dp(word1, m - 1, word2, n - 1)