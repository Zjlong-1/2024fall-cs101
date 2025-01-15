class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        k=m+n-2
        t=n-1
        ans=1
        for i in range(t+1,k+1):
            ans=ans*i/(i-t)
        return int(ans)