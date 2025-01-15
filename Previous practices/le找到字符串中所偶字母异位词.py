class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        n,m=len(s),len(p)
        if m>n:
            return []
        ds=defaultdict(int)
        dp=defaultdict(int)
        for i in range(m):
            ds[s[i]]+=1
            dp[p[i]]+=1
            dp[s[i]]+=0
        if ds==dp:
            ans.append(0)
        for i in range(n-m):
            ds[s[i]]-=1
            ds[s[i+m]]+=1
            dp[s[i+m]]+=0
            if ds==dp:
                ans.append(i+1)
        return ans
#加0使得两个字典中的长度一样（使得比大小变得可行）
#还可以自己写代码判断相等：
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)

        target_tb = defaultdict(int)
        for char in list(p):
            target_tb[char] += 1

        search_tb = defaultdict(int)
        for char in list(s[0:m - 1]):
            search_tb[char] += 1

        res = []

        for i in range(n - m + 1):
            search_tb[s[i + m - 1]] += 1
            flag = True
            for key, value in target_tb.items():
                if search_tb[key] == value:
                    continue
                else:
                    flag = False
                    break
            if flag:
                res.append(i)
            search_tb[s[i]] -= 1

        return res