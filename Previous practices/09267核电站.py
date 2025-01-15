n,m=map(int,input().split())
from functools import lru_cache
@lru_cache(maxsize=None)
def dfs(step,k):
    if step==m:
        return 0
    if step+n-k-1<m:
        return 2**(n-k-1)
    return dfs(step+1,k+1)+dfs(0,k+1)
print(dfs(0,-1))
#k表示已经走过的索引，所以一开始要从-1开始。
#还可以DP：如果第i位是不能放的，那么说明i-m这段区间肯定全放了，而且i-m-1这一位一定是0，因为如果该为是1的话就会在之前被处理掉，所以如果i为不能放，那么i-m-1这段区间的所有可能都需要从答案里减掉。那么状态转移方程就是：a[i]=2*a[i-1]-a[i-1-m]
# 23n1900014516
n, m = map(int, input().split())
DP = [0] * 60
DP[0] = 1 #DP[i]是第i个位置的方案数。

for i in range(1, n + 1):
    if i < m: #达不到连续放置m个的情况
        DP[i] = DP[i - 1] * 2  # 从第1个到第m-1个，方案都可以选择放/不放
    elif i == m: #第m个要小心了
        DP[i] = DP[i - 1] * 2 - 1
    else:#i>m
        DP[i] = DP[i - 1] * 2 - DP[i - m - 1]
print(DP[n])