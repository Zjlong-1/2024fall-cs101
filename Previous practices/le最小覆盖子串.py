class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if len(s)<len(t):
            return ''
        cnt1=Counter()
        cnt2=Counter(t)
        left1,right1=-1,len(s)-1
        left=0
        for i in range(len(s)):
            cnt1[s[i]]+=1
            while cnt1>=cnt2:
                if i-left<right1-left1:
                    left1,right1=left,i
                cnt1[s[left]]-=1
                left+=1
        if left1==-1:
            return ''
        return s[left1:right1+1]
#字典直接比大小！！！！！
#终极优化：而且cnt = defaultdict(int)  比 Counter 更快
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        res = (0,float('inf'))
        for j,c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:
                while True:
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:
                    res = (i,j)
                need[s[i]] += 1
                needCnt += 1
                i += 1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]