n=int(input())
l=[i for i in range(n,0,-1)]
def solve(n,l,t):
    k=l[t]
    if t==len(l)-1:
        return n//k
    ans = 0
    for i in range(n//k+1):
        ans+=solve(n-i*k,l,t+1)
    return ans
ans1=solve(n,l,0)
print(ans1)
#队列在函数递归中会出现问题，要改变l的承载形式，多加一个变量即可（用于记录位置）,好像改不对(难去重），递归很麻烦，DP更好。
# 创建dp表，dp[i][j]表示将i表示为不超过j的正整数之和的不同方式数
def solve(n):r
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= j:
                dp[i][j] += dp[i - j][j]
    return dp[n][n]
n = int(input())
print(solve(n))
#逻辑有问题，并不完备。要用递推来写：由前i个数分拆的方法数。
while True:
    try:
        n = int(input())
        l = [[1] * (n + 1)] + [[0] * (n + 1) for i in range(n - 1)]
        for i in range(1, n):
            for j in range(i + 1):
                l[i][j] = l[i - 1][j]
            for j in range(i + 1, n + 1):
                l[i][j] = l[i - 1][j] + l[i][j - i - 1]
        print(l[n - 1][n])
    except EOFError:
        break
#还可以简化空间复杂度，转化为一维数组。
while True:
    try:
        n = int(input())
        l = [1] * (n + 1)
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                l[j] = l[j] + l[j - i - 1]#注意这里的意义已经发生转变，对于固定的j ，j前面的指的是前i个的划分，而不是前i-1个
        print(l[n])
    except EOFError:
        break
#d递归可以做，但时间复杂度太高了：
from functools import lru_cache
while True:
    try:
        n=int(input())
        ans=0
        lru_cache(maxsize=None)
        def solve(i, x):
            global ans
            if i > x:
                return
            for j in range(i, x):
                solve(j, x - j)
            ans += 1
        solve(1, n)
        print(ans)
    except EOFError:
        break


