n,m=map(int,input().split())
l=list(map(int,input().split()))
i=1
la=[0]*(n+1)
t=False
mi=0
a=0
b=0
for k in range(1,n+1):
    la[k]=la[k-1]+l[k-1]
while i<=n:
    j=i
    while j<=n and la[j]-la[i-1]<=m:
        if la[j]-la[i-1]==m:
            t=True
            break
        else:j+=1
    if mi<la[j-1]-la[i-1]:
        mi=la[j-1]-la[i-1]
        a=i
        b=j-1
    if t:
        break
    i+=1
print(a,b,mi)
#超时了，可以部分优化，即j可已从上一个j开始。但好像有点小问题。
n,m=map(int,input().split())
l=list(map(int,input().split()))
i=1
la=[0]*(n+1)
t=False
mi=0
a=0
b=0
j=1
for k in range(1,n+1):
    la[k]=la[k-1]+l[k-1]
while i<=n:
    j-=1
    while j<=n and la[j]-la[i-1]<=m:
        if la[j]-la[i-1]==m:
            t=True
            break
        else:j+=1
    if mi<la[j-1]-la[i-1]:
        mi=la[j-1]-la[i-1]
        a=i
        b=j-1
    if t:
        break
    i+=1
print(a,b,mi)
#换算法，但思路一致：维护一个队列，让数组中的数依次入队，并记录其的元素和，若大于m,则让对首出列，更新答案，再让后面的数字继续入队，并更新答案，不断的这么操作，直到所有数字都入过队了为止。
#实际上就是双指针，和我一开始的思路一致。在此基础上，部分和变得没有很大作用。
from collections import deque
n, m = map(int, input().split())
a = list(map(int, input().split()))
q = deque()
sum_val = 0
ans1, ans2, ans3 = 0, 0, 0
l = 0
for i in range(n):
    q.append(a[i])
    sum_val += a[i]
    while sum_val > m:
        q.popleft()
        sum_val -= a[l]
        l += 1
    if sum_val > ans3:
        ans3 = sum_val
        ans1 = l + 1
        ans2 = i + 1
print(ans1, ans2, ans3)



