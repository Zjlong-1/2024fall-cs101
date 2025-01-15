import bisect
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l=[]
    l1.sort()#没用，还可能错（如果数据不友好，不是递增，就会出问题）
    for i in range(n):
        l.append((l1[i],l2[i]))
    l.sort()
    la=[0]*n
    la[0]=l[0][1]
    for i in range(1,n):
        m=bisect.bisect_left(l1,l1[i]-k)
        max1=l[i][1]
        for j in range(m):
            max1=max(la[j]+l[i][1],max1)
        la[i]=max1
    print(max(la))
#老套路，排序后以结尾的数为依据构建DP数组。
#但这种DP不是最好的，每次都没有记住，最好的是到前k个时最大收益。即扩大定义可以极大的节省计算。
from bisect import bisect_left

def max_profit(n, k, m, p):
    # dp[i] 表示前 i 个地点能获得的最大利润
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # 使用二分查找找到位置与 m[i-1] 至少差 k 的最大 j 值
        j = bisect_left(m, m[i-1] - k)  # 找到第一个小于 m[i-1] - k 的位置

        # 在 i 位置开餐馆的最大利润 (开和不开的最大值)
        dp[i] = max(dp[i-1], p[i-1] + dp[j])

    return dp[n]

# 主程序处理输入
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    m = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(max_profit(n, k, m, p))
