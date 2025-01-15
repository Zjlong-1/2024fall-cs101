# Assignment #B: Dec Mock Exam大雪前一天

Updated 1649 GMT+8 Dec 5, 2024

2024 fall, Complied by <mark>张俊龙，工学院</mark>



**说明：**

1）⽉考： AC6<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E22548: 机智的股民老张

http://cs101.openjudge.cn/practice/22548/

思路：DP，并实时维护最小值，贪心，每次减去前面最小的



代码：

```python
l=list(map(int,input().split()))
n=len(l)
la=[0]*n
min1=l[0]
for i in range(1,n):
    min1=min(min1,l[i])
    la[i]=max(la[i-1],l[i]-min1)
print(max(la))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### M28701: 炸鸡排

greedy, http://cs101.openjudge.cn/practice/28701/

思路：
分两种情况，一个是最大的不是很大，取平均值。另一个是最大的很大，这就转化为n-1的情况了


代码：

```python
n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
import sys
sys.setrecursionlimit(200000)
def solve(cnt,k):
    s=sum(l[cnt:])
    m=l[cnt]
    if k==1:
        return (f'{s:.3f}')
    if k==n:
        return (f'{min(l[cnt:]):.3f}')
    if m*k>s:
        return solve(cnt+1,k-1)
    else:
        return (f'{s/k:.3f}')
print(solve(0,k))
```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text](image-1.png)




### M20744: 土豪购物

dp, http://cs101.openjudge.cn/practice/20744/

思路：也是分两种情况，一种是拿出一个，另一种是不拿。事实上只要考虑两次贪心，
以第i个结尾的最大和，和以第i个开头的最大和



代码：

```python
l=list(map(int,input().split(',')))
n=len(l)
def solve():
    k=max(l)
    if k<0:
        return k
    la1=[-float('inf')]*n
    la2=la1[:]
    la1[0]=l[0]
    la2[-1] = l[-1]
    for i in range(1,n):
        la1[i]=max(la1[i-1]+l[i],l[i])
        la2[n-i-1]=max(la2[n-i]+l[n-i-1],l[n-i-1])
    ans=max(la1)
    for i in range(1,n-1):
        ans=max(ans,la1[i-1]+la2[i+1])
    return ans
print(solve())
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### T25561: 2022决战双十一

brute force, dfs, http://cs101.openjudge.cn/practice/25561/

思路：
dfs暴力枚举


代码：

```python
result = float("inf")
n, m = map(int, input().split())
store_prices = [input().split() for _ in range(n)]
you= [input().split() for _ in range(m)]
la=[0]*m
def dfs(i,sum1):
    global result
    if i==n:
        jian=0
        for i2 in range(m):
            store_j=0
            for k in you[i2]:
                a,b=map(int,k.split('-'))
                if la[i2]>=a:
                    store_j=max(store_j,b)
            jian+=store_j
        result=min(result,sum1-(sum1//300)*50-jian)
        return
    for i1 in store_prices[i]:
        idx,p=map(int,i1.split(':'))
        la[idx-1]+=p
        dfs(i+1,sum1+p)
        la[idx-1]-=p
dfs(0,0)
print(result)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




### T20741: 两座孤岛最短距离

dfs, bfs, http://cs101.openjudge.cn/practice/20741/

思路：dfs+bfs,考试时最后一步没有return一直runtime error。这里一个一个bfs显然会超时
要考虑超级源点，跟腐烂的橘子相似。



代码：

```python
from collections import deque
n=int(input())
l=[list(input())for _ in range(n)]
la=[[False]*n for _ in range(n)]
di=[(0,1),(0,-1),(1,0),(-1,0)]
f=deque()
def dfs(x,y):
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and  l[nx][ny]=='1':
            l[nx][ny]=2
            f.append((nx,ny))
            dfs(nx,ny)
def solve():
    for i in range(n):
        for j in range(n):
            if l[i][j]=='1':
                f.append((i,j))
                l[i][j]=2
                dfs(i,j)
                return
solve()
def bfs():
    ans=0
    while f:
        for _ in range(len(f)):
            x,y=f.popleft()
            for dx, dy in di:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n :
                    if l[nx][ny] == '1':
                        return ans
                    elif l[nx][ny]=='0':
                        l[nx][ny]=2
                        f.append((nx,ny))
        ans+=1
print(bfs())
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-3.png)



### T28776: 国王游戏

greedy, http://cs101.openjudge.cn/practice/28776

思路：两个连续的数组之间谁排前面可以由一个函数决定，以此函数排序在以此更新最大值。



代码：

```python
n=int(input())
a,b=map(int,input().split())
l=[]
for _ in range(n):
    x,y=map(int,input().split())
    l.append((x,y))
from functools import cmp_to_key
def compare(a1, b1, a2, b2):
    return (max(1 / b1, a1 / b2) >= max(1 / b2, a2 / b1)) - \
           (max(1 / b1, a1 / b2) < max(1 / b2, a2 / b1))
def compare_wrapper(x, y):
    return compare(x[0], x[1], y[0], y[1])
l = sorted(l, key=cmp_to_key(compare_wrapper))
ans=a//l[0][1]
for i in range(1,n):
    a*=l[i-1][0]
    b*=l[i-1][1]
    ans=max(ans,a//l[i][1])
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-4.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
这次考试有点崩，只AC了三个。孤岛问题的超级源点的思想其实在腐烂的橘子里面体现过，
但考试紧张没有回想起来导致一直超时，还有就是bfs忘记return了一直runtime error，
这浪费了大量时间，以至于最后一题看都没看，实际上最后一题感觉比较简单。双十一
没有把题目很好的抽象出来，一直暴力算，没有转化为dfs。总之，感觉对做过的题的掌握还有待加强
考试时不要一直卡在某个题上，有可能后面的更简单。




