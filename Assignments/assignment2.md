# Assignment #2: 语法练习

Updated 0126 GMT+8 Sep 24, 2024

2024 fall, Complied by ==张俊龙 工学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A



思路：分别考虑行，列的移动绝对值即可



##### 代码

```python
# n = 0
m = 0
for i in range(5):
    a = list(map(int, input().split()))
    if 1 in a:
        n=i
        m=a.index(1)
print(abs(2-n)+abs(2-m))

```



代码运行截图 ==（至少包含有"Accepted"）==

![alt text](IMG_20240929_114038-1.jpg)



### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A



思路：取模并加上即可



##### 代码

```python
# n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print((b-a%b)%b)

```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text](IMG_20240929_114038-2.jpg)




### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A



思路：一步一步来，判断与0的大小



##### 代码

```python
# n=int(input())
m=input().split()
t=0
k=0
for i in range(n):
    t=t+int(m[i])
    if t<0:
        k+=1
        t=t+1
print(k)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](IMG_20240929_114057_edit_1922553055394571-1.jpg)



### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：将题目抽象化，不断合并区间



##### 代码

```python
# n,m=map(int,input().split())
l=[]
a=0
for i in range(m):
    j,k=map(int,input().split())
    l.append((j,k))
l.sort()
for o in range(m-1):
    if l[o][1]>=l[o+1][0]:
        l[o+1]=(l[o][0],max(l[o+1][1],l[o][1]))
        l[o]=(0,0)
while (0,0) in l:
    l.remove((0, 0))
for u in range(len(l)):
    a=a+l[u][1]+1-l[u][0]
print(n-a+1)
print(l)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==
![alt text](IMG_20240929_114145-1.jpg)




### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60



思路：按题目来，判断是否成立即可



##### 代码

```python
# a,b=map(int,input().split())
l=[]
for i in range(a,b+1):
    q=i//100
    w=(i%100)//10
    e=i%10
    if q**3+w**3+e**3==i:
        l.append(i)
if len(l)==0:
        print('NO')
else:
        print(*l)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==
![alt text](IMG_20240929_114337-1.jpg)




### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/



思路：一开始十分无助，想着什么时候追上，什么时候换人。但最后细想发现只要找出最短时间并且起跑>=0的人即可（跟谁跑就会跟谁一起打终点）



##### 代码

```python
# import math
while True:
    n=int(input())
    if n==0:
        break
    l=[]
    for i in range(n):
        t=0
        a,b=map(int,input().split())
        if b>=0:
            t=b+math.ceil(16200/a)
            l.append(t)
    print(min(l))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](IMG_20240929_121038_edit_1923154363709967-1.jpg)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

终于赶上进度了，经过这段时间的刷题，对python的语法变得熟练了，而且敲代码的速度也越来越快，思路也变得清晰起来。跟着ChatGPT也学习了许多python中的内置函数。最近自己也开始自己找题做（OJ，CF），喜欢上了敲代码的感觉。



