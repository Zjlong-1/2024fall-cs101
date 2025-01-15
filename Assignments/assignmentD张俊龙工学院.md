# Assignment #D: 十全十美 

Updated 1254 GMT+8 Dec 17, 2024

2024 fall, Complied by <mark>张俊龙，工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02692: 假币问题

brute force, http://cs101.openjudge.cn/practice/02692

思路：
这个题目要注意到假币的独有性质，假币在天平上就会不平衡，不在才会平衡。


代码：

```python
n=int(input())
for y in range(n):
    l = [[], [], []]
    for i in range(3):
        l[i] = input().split()
    for k in 'ABCDEFGHIJKL':
        if all((k in i[0] and i[2] == 'up') or (k in i[1] and i[2] == 'down') or (k not in i[0]+i[1] and i[2] == 'even')  for i in l):
            print('{} is the counterfeit coin and it is {}.'.format(k, 'heavy'))
        if all((k in i[0] and i[2] == 'down') or (k in i[1] and i[2] == 'up') or (k not in i[0]+i[1] and i[2] == 'even') for i in l):
            print('{} is the counterfeit coin and it is {}.'.format(k, 'light'))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### 01088: 滑雪

dp, dfs similar, http://cs101.openjudge.cn/practice/01088

思路：就是普通的dp+dfs



代码：

```python
r,c=map(int,input().split())
l=[]
l2=[]
for i in range(r):
    l1=list(map(int,input().split()))
    for j in range(c):
        l.append((l1[j],i,j))
    l2.append(l1)
l.sort()
la=[[1]*c for _ in range(r)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for a,b,d in l:
    for dx, dy in directions:
        b1, d1 = b+ dx, d+ dy
        if 0 <= b1 < r and 0 <=d1 < c and l2[b1][d1] < a:
            la[b][d] = max(la[b][d], la[b1][d1] + 1)
print(max(la[i][j] for i in range(r) for j in range(c)))
```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text](image-3.png)




### 25572: 螃蟹采蘑菇

bfs, dfs, http://cs101.openjudge.cn/practice/25572/

思路：bfs,每次储存两个点



代码：

```python
from collections import deque
n=int(input())
l=[]
cnt=0
l2=[(0,0),(0,0)]
for i in range(n):
    l1=list(map(int,input().split()))
    l.append(l1)
    if cnt!=2:
        for j in range(n):
            if l1[j]==5:
                l2[cnt]=(i,j)
                cnt+=1
x1,y1,x2,y2=l2[0][0],l2[0][1],l2[1][0],l2[1][1]
d=[(0,1),(0,-1),(-1,0),(1,0)]
q=deque()
inq=set()
def solve(x1,y1,x2,y2):
    q.append((x1,y1,x2,y2))
    inq.add((x1,y1,x2,y2))
    while q:
        x3,y3,x4,y4=q.popleft()
        if l[x3][y3]==9 or l[x4][y4]==9:
            return True
        for dx,dy in d:
            nx1,ny1,nx2,ny2=x3+dx,y3+dy,x4+dx,y4+dy
            if 0<=nx1<n and 0<=nx2<n and 0<=ny1<n and 0<=ny2<n and l[nx1][ny1]!=1 and l[nx2][ny2]!=1 and (nx1,ny1,nx2,ny2) not in inq:
                q.append((nx1,ny1,nx2,ny2))
                inq.add((nx1,ny1,nx2,ny2))
    return False
if solve(x1,y1,x2,y2):
    print('yes')
else:
    print('no')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-4.png)



### 27373: 最大整数

dp, http://cs101.openjudge.cn/practice/27373/

思路：构造映射，按照此映射排序再组合即可



代码：

```python
def f(x):
    return int(x)/(10**(len(x))-1)
m=int(input())
n=int(input())
l=list(input().split())
l.sort(key=lambda x:-f(x))
la=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        k=len(l[i-1])
        if k>j:
            la[i][j]=la[i-1][j]
        else:
            la[i][j]=max(la[i-1][j],la[i-1][j-k]*(10**k)+int(l[i-1]))
print(la[-1][-1])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-5.png)



### 02811: 熄灯问题

brute force, http://cs101.openjudge.cn/practice/02811

思路：#注意到，在第一行开关灯确定之后，要想熄灯，那么后面n-1行的操作是固定的，所以只要枚举2**6次即可。先定义某个点的熄灯操作，反正就是一层一层，一次一次地操作



代码：

```python

dx,dy=[0,0,-1,1,0],[0,-1,0,0,1]
def p(light,x,y):
    for i in range(5):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<5 and 0<=ny<6:
            light[nx][ny]^=1
def solve():
    for j in range(64):
        s=[row[:] for row in light]
        solution=[[0]*6 for _ in range(5)]
        for x in range(6):
            if (j >>x)&1:
                solution[0][x]=1
                p(s,0,x)
        for i in range(1,5):
            for j in range(6):
                if s[i-1][j]==1:
                    solution[i][j]=1
                    p(s,i,j)
        if all(s[4][j]==0 for j in range(6)):
            for i in solution:
                print(*i)
light=[[int(i) for i in input().split()] for _ in range(5)]
solve()
  

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### 08210: 河中跳房子

binary search, greedy, http://cs101.openjudge.cn/practice/08210/

思路：

确定差距一个一个尝试（用二分法实现）

代码：

```python
l,n,m=map(int,input().split())
lens=[0]+[int(input()) for _ in range(n)]+[l]
def can(d):
    idx=0
    cnt=0
    for i in range(1,n+2):
        if lens[i]-lens[idx]>=d:
            idx=i
        else:
            cnt+=1
    if cnt<=m:
        return True
    return False
left=0
right=l
while left<right:
     t=(left+right)//2+1
     if can(t):
         left=t
     else:
         right=t-1
print(left)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
最近已经把每日选做写完了，目前主要是写leetcode上面的题，考前几天打算把栈和堆再复习一下，感觉还是要多刷题保持手感。




