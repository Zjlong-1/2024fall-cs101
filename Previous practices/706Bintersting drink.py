n=int(input())
l=list(map(int,input().split()))
l.sort()
q=int(input())
for i in range(q):
    t=int(input())
    ans=0
    for k in l:
        if k>t:
            break
        ans+=1
    print(ans)
#超时了，考虑用字典存储位置，再重组排列
n = int(input())
l = list(map(int, input().split()))
l.sort()
q = int(input())
k = []
for i in range(q):
    t = int(input())
    k.append((i, t))
k.sort(key=lambda x: x[1])
s = 0
ans=[]
for i in range(q):
    for j in range(s, n):
        if k[i][1] < l[j]:
            ans.append((k[i][0],j))
            s = max(j - 1,0)
            break
        if j==n-1:
            ans.append((k[i][0],n))
ans.sort()
for i in ans:
    print(i[1])
#还是超时了！！！！！
#可以用内置函数二分查找：
import bisect

n = int(input())
x = [int(_) for _ in input().split()]
x.sort()

for _ in range(int(input())):
    m = int(input())
    print(bisect.bisect_right(x, m)
#常规法：dp,非常巧妙，用一来量化
    n = int(input())
    l = list(map(int, input().split()))
    q = int(input())
    l1 = [int(input()) for _ in range(q)]
    k = [0] * 100001
    for i in l:
        k[i] += 1
    for i in range(1, 100001):
        k[i] += k[i - 1]
    for t in l1:
        if
    t >= 100001:
    print(k[-1])
    else:
    print(k[t])





