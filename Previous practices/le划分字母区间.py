class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        from collections import defaultdict
        l=defaultdict(int)
        n=len(s)
        for i in range(n):
            l[s[i]]=i
        k=0
        end=0
        start = 0
        ans=[]
        while k<n:
            end=max(l[s[k]],end)
            if k==end:
                ans.append(end-start+1)
                start=k+1
            k+=1
        return ans
#记录结尾并不断更新，如果走到了结尾，就可以返回一个值。