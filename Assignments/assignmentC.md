# Assignment #C: 五味杂陈 

Updated 1148 GMT+8 Dec 10, 2024

2024 fall, Complied by <mark>张俊龙，工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 1115. 取石子游戏

dfs, https://www.acwing.com/problem/content/description/1117/

思路：[a/b]≥2, 则先手有选择权，可以切换到必胜的情况，设a=t*b+r,0<=r<b,(r,b)只有胜与不胜两种可能，
如果(r,b)胜，则先手转化为（b+r,b）就可以必胜，如果（r,b）败，转化为（r,b）就可以必胜
至于[a/b]<=1时就递归




代码：

```python
def solve(a,b):
    a,b=min(a,b),max(a,b)
    if b%a==0:
        return True
    k=b//a
    if k>=2:
        return True
    else:
        return not solve(a,b-a)
while True:
    a,b=map(int,input().split())
    if a==b==0:
        break
    if solve(a,b):
        print('win')
    else:
        print('lose')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### 25570: 洋葱

Matrices, http://cs101.openjudge.cn/practice/25570

思路：暴力一层一层算，记录结果后取max



代码：

```python
n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
def solve(x):
    k=0
    for i in range(x,n-x):
        k+=l[i][x]+l[i][n-1-x]
    for i in range(x+1,n-1-x):
        k+=l[x][i]+l[n-1-x][i]
    return k
if n%2==0:
    print(max(solve(i) for i in range(n//2)))
elif n==1:
    print(l[0][0])
else:
    ans=max(solve(i) for i in range(n//2))
    print(max(ans,l[n//2][n//2]))
```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text](image-1.png)




### 1526C1. Potions(Easy Version)

greedy, dp, data structures, brute force, *1500, https://codeforces.com/problemset/problem/1526/C1

思路：这个题目没有想到用后悔算法，直接DP做的。考虑前i个里喝j 个的体力最大值,而且是在可行的前提下



代码：

```python
n = int(input())
l = list(map(int, input().split()))
dp = [-1] * (n + 1)
dp[0] = 0 
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        if dp[j - 1] >= 0:
            dp[j] = max(dp[j], dp[j - 1] + l[i - 1])
for i in range(n, -1, -1):
    if dp[i] >= 0:
        print(i)
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-2.png)



### 22067: 快速堆猪

辅助栈，http://cs101.openjudge.cn/practice/22067/

思路：辅助栈



代码：

```python
s1,s2=[],[]
while True:
    try:
        l=input().split()
    except EOFError:
        break
    if l[0]=='pop' and s1:
        s1.pop()
        s2.pop()
    elif l[0]=='min' and s2:
        print(s2[-1])
    elif l[0]=='push':
        k=int(l[1])
        s1.append(k)
        if s2:
            s2.append(min(s2[-1],k))
        else:
            s2.append(k)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### 20106: 走山路

Dijkstra, http://cs101.openjudge.cn/practice/20106/

思路：dijksra,套模板就可以了



代码：

```python
import heapq
m,n,p=map(int,input().split())
l=[input().split() for _ in range(m)]
di=[(0,1),(0,-1),(1,0),(-1,0)]
def solve(x1,y1,x2,y2):
    heap=[]
    la=[[float('inf')]*n for _ in range(m)]
    if l[x1][y1]=='#' or l[x2][y2]=='#':
        return 'NO'
    la[x1][y1]=0
    heapq.heappush(heap,(0,x1,y1))
    while heap:
        d,x,y=heapq.heappop(heap)
        if x==x2 and y==y2:
            return d
        k=int(l[x][y])
        for dx,dy in di:
            nx,ny=dx+x,dy+y
            if 0<=nx<m and 0<=ny<n and l[nx][ny]!='#':
                if la[nx][ny]>d+abs(k-int(l[nx][ny])):
                    la[nx][ny]=d+abs(k-int(l[nx][ny]))
                    heapq.heappush(heap,(la[nx][ny],nx,ny))
    return 'NO'
for _ in range(p):
    x1, y1, x2, y2=map(int,input().split())
    print(solve(x1,y1,x2,y2))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)




### 04129: 变换的迷宫

bfs, http://cs101.openjudge.cn/practice/04129/

思路：
要多加一个维度，在取模的意义下判断


代码：

```python
from collections import deque
di=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(x,y):
    q=deque()
    inq=set()
    q.append((0,x,y))
    inq.add((0,x,y))
    while q:
        ti,x,y=q.popleft()
        for dx,dy in di:
            nx,ny=dx+x,dy+y
            kt=(ti+1)%k
            if 0<=nx<r and 0<=ny<c and (kt,nx,ny) not in inq:
                if l[nx][ny]=='E':
                    return ti+1
                elif l[nx][ny]!='#' or kt==0:
                    q.append((ti+1,nx,ny))
                    inq.add((kt,nx,ny))
    return 'Oop!'
t=int(input())
for _ in range(t):
    r, c, k = map(int, input().split())
    l = [list(input()) for i in range(r)]
    def solve():
        for i in range(r):
            for j in range(c):
                if l[i][j]=='S':
                    print(bfs(i,j))
                    return
    solve()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
最近pre比较多，没有时间额外刷题了，只把每日选做做到了12.20。下周争取多刷一点题保持手感。




