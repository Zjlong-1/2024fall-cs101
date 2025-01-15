#又是一个很难的滑动窗口题,先每个减去520转化为求和为0的最长连续子序列,这就转化为求最大连续和的问题了（current_sum-min)
from collections import defaultdict
n=int(input())
l=list(map(int,input().split()))
gift=[i-520 for i in l]
d=defaultdict(list)
d[0].append(-1)
sum1=0
ans=0
for i in range(n):
    sum1+=gift[i]
    if sum1 in d:
        ans=max(ans,i-d[sum1][0])
    d[sum1].append(i)
print(ans*520)
