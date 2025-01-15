# Assignment #A: dp & bfs

Updated 2 GMT+8 Nov 25, 2024

2024 fall, Complied by <mark>张俊龙，工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：
斐波拉切数列，用DP实现


代码：

```python
n=int(input())
a,b=1,2
for i in range(n-2):
    a,b=b,a+b
if n==1:
    print(a)
else:
    print(b)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：dp和递归都可以，因为懒得多构建列表所以直接递归（时间慢一点）



代码：

```python
from functools import lru_cache
lru_cache(maxsize=None)
def solve(n):
    if n==1:
        return 1
    return sum(solve(i) for i in range(1,n))+1
n=int(input())
print(solve(n))
```



代码运行截图 ==（至少包含有"Accepted"）==

![alt text](image-1.png)



### 474D. Flowers

dp, https://codeforces.com/problemset/problem/474/D

思路：每次都有sum会超时，要用前缀和，每一次都有取模。



代码：

```python
t,k=map(int,input().split())
l=[0]*(10**5+1)
s=[0]*(10**5+1)
l[0]=1
for i in range(1,k):
    l[i]=1
    s[i]=(s[i-1]+l[i])%(10**9+7)
for i in range(k,10**5+1):
    l[i]=(l[i-1]+l[i-k])%(10**9+7)
    s[i]=(s[i-1]+l[i])%(10**9+7)
for _ in range(t):
    a,b=map(int,input().split())
    print((s[b]-s[a-1])%(10**9+7))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




### LeetCode5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：双指针，从中间扩散



代码：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans=1
        anss=s[0]
        if n==1:
            return s
        if s[0]==s[1]:
            ans=2
            anss=s[:2]
        for i in range(1,n-1):
            if s[i]==s[i+1]:
                left,right=i-1,i+2
                k=2
                while 0<=left and right<n:
                    if s[left]==s[right]:
                        k+=2
                        left-=1
                        right+=1
                    else:break
                if ans<k:
                    anss=s[left+1:right]
                    ans=k
            if  s[i-1]==s[i+1]:
                k=3 
                left,right=i-2,i+2
                while 0<=left and right<n:
                    if s[left]==s[right]:
                        k+=2
                        left-=1
                        right+=1
                    else:break
                if ans<k:
                    anss=s[left+1:right]
                    ans=k
        return anss
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-2.png)





### 12029: 水淹七军

bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：dfs，多添一个水深列表



代码：

```python
import sys
sys.setrecursionlimit(800000)
input=sys.stdin.read
data=input().split()
k=int(data[0])
id=1
for _ in range(k):
    m,n=map(int,data[id:id+2])
    id+=2
    l=[]
    for i in range(m):
        l.append(list(map(int,data[id:id+n])))
        id+=n
    i1, j1 = map(int, data[id:id + 2])
    id += 2
    p=int(data[id])
    id+=1
    wh=[[0]*n for i in range(m)]
    l1=[(-1,0),(1,0),(0,1),(0,-1)]
    def solve(x,y):
        for dx,dy in l1:
            nx,ny=dx+x,dy+y
            if 0<=nx<m and 0<=ny<n and l[nx][ny]<wh[x][y] and wh[nx][ny]<wh[x][y]:
                wh[nx][ny]=wh[x][y]
                solve(nx,ny)
    for i in range(p):
        x,y=map(int,data[id:id+2])
        id+=2
        x-=1
        y-=1
        if wh[x][y]<l[x][y]:
            wh[x][y]=l[x][y]
            solve(x,y)
    if wh[i1-1][j1-1]!=0:
        print('Yes')
    else:
        print('No')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-3.png)



### 02802: 小游戏

bfs, http://cs101.openjudge.cn/practice/02802/

思路：bfs暴力枚举，把步数换为边数并单独储存，最后取MIM



代码：

```python
from collections import deque
board=1
while True:
    w,h=map(int,input().split())
    if w==h==0:
        break
    l=[[' ']*(w+2) for _ in range(h+2)]
    for i in range(1,h+1):
        k=input()
        for j in range(len(k)):
            l[i][j+1]=k[j]
    print(f'Board #{board}:')
    board+=1
    l1=[(0,1,1),(0,-1,2),(1,0,3),(-1,0,4)]
    def bfs(x1,x2,y1,y2):
        ans=[]
        inq=set()
        q=deque()
        q.append((0,y1,x1,-1))
        while q:
            step,y,x,direction1=q.popleft()
            for dx,dy,direction2 in l1:
                nx,ny=dx+x,dy+y
                if 0<=ny<h+2 and 0<=nx<w+2 and (ny,nx,direction2) not in inq :
                    step1 = step
                    if direction1!=direction2:
                        step1=step+1
                    if nx==x2 and ny==y2:
                        ans.append(step1)
                        continue
                    if l[ny][nx]!='X':
                        inq.add((ny, nx,direction2))
                        q.append((step1, ny, nx, direction2))
        if len(ans)==0:
            return 0
        else:
            return min(ans)
    pair=1
    while True:
        x1,y1,x2,y2=map(int,input().split())
        if x1==x2==y1==y2==0:
            break
        k=bfs(x1,x2,y1,y2)
        if k:
            print(f'Pair {pair}: {k} segments.')
        else:
            print(f'Pair {pair}: impossible.')
        pair+=1
    print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
前面4个比较简单，水淹七军的数据读入卡了好久，水深的实时更新也是debug出来的。小游戏的输出好折磨人，一开始根本没看到print()导致总是不对
最近主要是做了leetcode上的一些dp和栈的题目：115,1035，394,739,215




