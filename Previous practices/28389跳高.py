n=int(input())
l=list(map(int,input().split()))
la=[l[0]]
ans=1
for i in range(n):
    t=-1
    for j in range(len(la)):
        if l[i]>=la[j]:
            t=j
            break
    if t==-1:
        la.append(l[i])
        ans+=1
    else:
        la[t]=l[i]
print(ans)
#上网搜找到sortedliist,本质就是提示给的二分查找。但python中没有此内置库，只能手动二分查找。
#Dilworth定理:
#Dilworth定理表明，任何一个有限偏序集的最长反链(即最长下降子序列)的长度，
#等于将该偏序集划分为尽量少的链(即上升子序列)的最小数量。
#因此，计算序列的最长下降子序列长度，即可得出最少需要多少台测试仪
#非常巧妙的自动排序+贪心优化：
from bisect import bisect_left
n=int(input())
l=list(map(int,input().split()))
l.reverse()
la=[]
for i in l:
    t=bisect_left(la,i)
    if t<len(la):
        la[t]=i
    else:
        la.append(i)
print(len(la))