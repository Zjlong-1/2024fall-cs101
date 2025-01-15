from collections import Counter
n=int(input())
l=list(map(int,input().split()))
s=Counter(l)
s=sorted(s.items())
la=[0]*(len(s)+1)
la[1]=s[0][0]*s[0][1]
for i in range(2,len(s)+1):
    if s[i-1][0]==s[i-2][0]+1:
        la[i]=max(la[i-1],la[i-2]+s[i-1][1]*s[i-1][0])
    else:
        la[i]=la[i-1]+s[i-1][1]*s[i-1][0]
print(la[len(s)])
#DP即可，但注意积累Counter字典对元素排序转化为元素对列表的方法。前面i个（不在乎第i个的状态，这一般是比较好的想法）最大的可能。
#另一思路：第I个选与不选。将每个数的出现次数统计出来，然后用动态规划来解决“选择不相邻数的最大和”问题。通过维护两个状态 dp[i][0] 和 dp[i][1]，分别记录不选择和选择当前数时的最大和，从而逐步构建最终的解。
# 高景行 24数学科学学院
M = int(1e5)
a = [0] * (M + 1)
n = int(input())
for x in map(int, input().split()): a[x] += 1
dp = [[0, 0] for _ in range(M + 1)]
# dp[i][0] 不选i, dp[i][1] 选i
for i in range(1, M + 1):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
    dp[i][1] = dp[i - 1][0] + a[i] * i
print(max(dp[M][0], dp[M][1]))
#如果不想判断，也可以统一弄：（但空间复杂度比较的大）
input()
c = [0] * 100001
for m in map(int, input().split()):
    c[m] += 1

dp = [0] * 100001
for i in range(1, 100001):
    dp[i] = max(dp[i - 1], dp[i - 2] + i * c[i])

print(max(dp))

