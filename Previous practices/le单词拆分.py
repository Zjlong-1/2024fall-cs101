class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        la=[False]*(n+1)
        la[0]=True
        for i in range(n+1):
            for j in range(i+1):
                if   la[j] and s[j:i] in wordDict:
                    la[i]=True
        return la[-1]
#优化版：
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def do(si):
            if si >= len(s):
                return True
            for w in wordDict:
                wl = len(w)
                if s[si:si + wl] == w and do(si + wl):
                    return True
            return False

        return do(0)