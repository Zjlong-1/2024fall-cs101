class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        la=[1]*len(s)
        k=set()
        k.add(s[0])
        for i in range(1,len(s)):
            if s[i] not in k:
                la[i]=la[i-1]+1
                k.add(s[i])
            else:
                k.clear()
                k.add(s[i])
                for j in range(i-1,0,-1):
                    if s[j]==s[i]:
                        break
                    else:
                        k.add(s[j])
                la[i]=len(k)
        return max(la)
#优化：滑动窗口，确定起点与终点（双指针），于是只需要remove 一个就好了：
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

