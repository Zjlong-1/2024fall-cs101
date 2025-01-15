# Assignment #9: dfs, bfs, & dp

Updated 2107 GMT+8 Nov 19, 2024

2024 fall, Complied by <mark>张俊龙，工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 18160: 最大连通域面积

dfs similar, http://cs101.openjudge.cn/practice/18160

思路：dfs,套模版，实时更新最大值。



代码：

```python
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l=[list(input()) for i in range(n)]
    l1=[(0,1),(0,-1),(1,1),(1,0),(1,-1),(-1,0),(-1,-1),(-1,1)]
    def dfs(x,y):
        global cnt
        cnt += 1
        for dx,dy in l1:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and l[nx][ny]=='W':
                l[nx][ny]='.'
                dfs(nx,ny)
    ans=0
    for i in range(n):
        for j in range(m):
            if l[i][j]=='W':
                l[i][j]='.'
                cnt=0
                dfs(i,j)
                ans=max(ans,cnt)
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930

思路：
最短步，bfs.


代码：

```python
from collections import deque
m,n=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(m)]
l1=[(1,0),(0,1),(0,-1),(-1,0)]
def bfs(x,y):
    q=deque()
    step=0
    inq=set()
    q.append((step,(x,y)))
    inq.add((x,y))
    while q:
        step,(x,y)=q.popleft()
        if l[x][y]==1:
            return step
        for dx,dy in l1:
            nx,ny=dx+x,dy+y
            if 0<=nx<m and 0<=ny<n and l[nx][ny]!=2 and (nx,ny) not in inq:
                inq.add((nx,ny))
                q.append((step+1,(nx,ny)))
    return 'NO'
print(bfs(0,0))
```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text](image-1.png)




### 04123: 马走日

dfs, http://cs101.openjudge.cn/practice/04123

思路：dfs+回溯



代码：

```python
t=int(input())
for _ in range(t):
    n,m,x,y=map(int,input().split())
    k=m*n
    l=[[False]*m for i in range(n)]
    l1=[(1,2),(1,-2),(-1,-2),(-1,2),(2,1),(2,-1),(-2,1),(-2,-1)]
    ans=0
    def dfs(x,y,step):
        global ans
        if step==k:
            ans+=1
        for dx,dy in l1:
            nx,ny=dx+x,dy+y
            if 0<=nx<n and 0<=ny<m and not l[nx][ny]:
                l[nx][ny]=True
                dfs(nx,ny,step+1)
                l[nx][ny]=False
    l[x][y]=True
    dfs(x,y,1)
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### sy316: 矩阵最大权值路径

dfs, https://sunnywhy.com/sfbj/8/1/316

思路：dfs+回溯，要注意列表也要global



代码：

```python
n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
ans=-float('inf')
ansl=[]
visit=[[False]*m for _ in range(n)]
l1=[(0,1),(0,-1),(1,0),(-1,0)]
def dfs(x,y,sum,way):
    global ans,ansl
    if x==n-1 and y==m-1:
        if ans<sum:
            ans=sum
            ansl=way[:]
    for dx,dy in l1:
        nx,ny=dx+x,dy+y
        if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
            visit[nx][ny]=True
            dfs(nx,ny,sum+l[nx][ny],way+[(nx+1,ny+1)])
            visit[nx][ny]=False
visit[0][0]=True
dfs(0,0,0,[(1,1)])
for i,j in ansl:
    print(i,j)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-3.png)





### LeetCode62.不同路径

dp, https://leetcode.cn/problems/unique-paths/

思路：数学思想，向下向上走的步数是确定的，只要计算组合数就可以了。



代码：

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        k=m+n-2
        t=n-1
        ans=1
        for i in range(t+1,k+1):
            ans=ans*i/(i-t)
        return int(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-4.png)



### sy358: 受到祝福的平方

dfs, dp, https://sunnywhy.com/sfbj/8/3/539

思路：数据量比较小，所以可以暴力dfs



代码：

```python
import sys
sys.setrecursionlimit(10*6)
from math import sqrt
def square(x):
    return  int(sqrt(x))**2==x!=0
t=input()
n=len(t)
def solve(i):
    for j in range(i,n):
        if square(int(t[i:j+1])):
            if j==n-1:
                return True
            if solve(j+1):
                return True
    return False
if solve(0):
    print('Yes')
else:
    print('No')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
因为在之前把leetcode上回溯的题刷完了，所以作业做得比较顺畅。发现多做几个题有利于掌握dfs和bfs，熟悉模版就写得比较快。
额外做了leetcode:560,239,76,41,53,46,78,22,39,79



