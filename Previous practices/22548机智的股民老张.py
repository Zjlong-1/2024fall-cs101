l=list(map(int,input().split()))
n=len(l)
la=[0]*n
min1=l[0]
for i in range(1,n):
    min1=min(min1,l[i])
    la[i]=max(la[i-1],l[i]-min1)
print(max(la))
#DP，并实时维护最小值
#有一点妙的优化：
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        max_p = min_p = prices[0]
        ans = 0
        for price in prices:

            if price < min_p:
                max_p = min_p = price
                continue

            if price > max_p:
                max_p = price
                ans = max(ans, max_p - min_p)

        return ans

