n,k,d=map(int,input().split())
def solve(n,k,d):
    l1 = [0] * (n + 1)
    l2 = [0] * (n + 1)
    l1[0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            l1[i] += l1[i - j]
    if d>n:
        return 0
    l2[d]=1
    for i in range(d + 1, n + 1):
        for j in range(1, d):
            l2[i] += l2[i - j]
        for j in range(d, min(i, k) + 1):
            l2[i] += l1[i - j]
    return l2[-1]%(10**9+7)
print(solve(n,k,d))
#就是一个数列题，但要注意d大于n 时没有解。

# 23工学院 蒋子轩
n,k,d=map(int,input().split())
mod = 10**9 + 7
# A[i]：总权重为i的路径数 ； B[i]：总权重为i且所有边权重小于d的路径数
A = [1] + [0] * n
B = [1] + [0] * n
# 路径数本质上就是整数划分问题
# 本题即求用不大于k的正整数划分i，用小于d的正整数划分i的方法数之差
for i in range(1, n + 1):
    for j in range(1, min(i,k)+1):
        A[i] = (A[i] + A[i - j]) % mod
    for j in range(1, min(d, i + 1)):
        B[i] = (B[i] + B[i - j]) % mod
print((A[n] - B[n]) % mod)



