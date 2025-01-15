class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans=1
        anss=s[0]
        if n==1:
            return s
        if s[0]==s[1]:
            ans=2
            anss=s[:2]
        for i in range(1,n-1):
            if s[i]==s[i+1]:
                left,right=i-1,i+2
                k=2
                while 0<=left and right<n:
                    if s[left]==s[right]:
                        k+=2
                        left-=1
                        right+=1
                    else:break
                if ans<k:
                    anss=s[left+1:right]
                    ans=k
            if  s[i-1]==s[i+1]:
                k=3
                left,right=i-2,i+2
                while 0<=left and right<n:
                    if s[left]==s[right]:
                        k+=2
                        left-=1
                        right+=1
                    else:break
                if ans<k:
                    anss=s[left+1:right]
                    ans=k
        return anss