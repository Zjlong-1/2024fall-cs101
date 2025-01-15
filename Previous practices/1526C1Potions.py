n=int(input())
l=list(map(int,input().split()))
#前i个里喝j 个的体力最大值,而且是在可行的前提下
la=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,i):
        if la[i-1][j-1]<0:
            la[i][j]=la[i-1][j]
        else:
            la[i][j]=max(la[i-1][j-1]+l[i-1],la[i-1][j])
    if la[i-1][i-1]<0:
        la[i][i]=-1
    else:
        la[i][i]=la[i-1][i-1]+l[i-1]
for i in range(n,-1,-1):
    if la[-1][i]>=0:
        print(i)
        break
#超时了，-1的赋值可以在一开始就用上，而且可以用滚动数组：
n = int(input())
l = list(map(int, input().split()))

# dp[j] 表示选 j 个时的最大体力值
dp = [-1] * (n + 1)
dp[0] = 0  # 选 0 个的体力值为 0

for i in range(1, n + 1):
    # 倒序更新 dp 防止覆盖
    for j in range(i, 0, -1):
        if dp[j - 1] >= 0:
            dp[j] = max(dp[j], dp[j - 1] + l[i - 1])

# 找到最大的 j 使得 dp[j] >= 0
for i in range(n, -1, -1):
    if dp[i] >= 0:
        print(i)
        break
#刚好卡时间过了，还可以用函数来加快。
#还可以贪心反悔算法，快了十倍：
import heapq


def max_potions(n, potions):
    # 当前健康值
    health = 0
    # 已经饮用的药水效果列表，用作最小堆
    consumed = []

    for potion in potions:
        # 尝试饮用当前药水
        health += potion
        heapq.heappush(consumed, potion)
        if health < 0:
            # 如果饮用后健康值为负，且堆中有元素
            if consumed:
                health -= consumed[0]
                heapq.heappop(consumed)


    return len(consumed)

n = int(input())
potions = list(map(int, input().split()))
print(max_potions(n, potions))
