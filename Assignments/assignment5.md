# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>张俊龙，工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：
没什么技巧，一一判断即可


代码：

```python
k=0
while True:
    k+=1
    a,b,c,d=map(int,input().split())
    if a==b==c==d==-1:
        break
    t=0
    while (t+d-a)%23!=0 or (t+d-b)%28!=0 or (t+d-c)%33!=0 or t==0:
        t+=1
    print('Case {}: the next triple peak occurs in {} days.'.format(k,t))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text]({A5908B5D-4570-45C7-8A89-7F28EC2E4A64}.png)




### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：
感觉要双指针，做最便宜的，卖最贵的


代码：

```python
p=int(input())
l=list(map(int,input().split()))
l.sort()
n=len(l)
i=0
j=n-1
ans=0
while True:
    while i<n and p >= l[i]:
        p -= l[i]
        i += 1
        ans+=1
    if  ans>=1 and j>i :
        p+=l[j]-l[i]
        j-=1
        i+=1
    else:
        break
print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text]({7DDC34BA-FCE4-46A6-8FEF-D217518A9080}.png)




### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：
排序后贪心，越前面权重越大，所以最小放最前。


代码：

```python
n=int(input())
l=list(map(int,input().split()))
la=[]
for i in range(n):
    la.append((l[i],i+1))
la.sort(key=lambda x :(x[0],x[1]))
print(' '.join(str(la[i][1]) for i in range(n)))
k=sum(la[i][0]*(n-1-i) for i in range(n))
print(f'{k/n:.2f}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text]({82FE9083-8AF2-406A-AA74-F6F0CDF16F20}.png)




### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：
把一个周期的所有情况弄出来，再将所有情况化归于此


代码：

```python
A = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax',
     'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
B = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk',
     'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
C = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
D = {}
for i in range(260):
    D[i] = C[i % 13-1]+' '+B[i % 20-1]
n=int(input())
print(n)
for _ in range(n):
    l=input().split()
    t=int(l[0][:-1])+1+int(l[2])*365+A.index(l[1])*20
    print(D[t%260]+' '+str((t-1)//260))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text]({90D37323-685D-491F-8C7E-AC999AF7576A}.png)



### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：
最左边排左边，以此思路不断递推，从简单入手，先把左边尽可能砍掉（可以说明这种方式不比任何方式差）


代码：

```python
n=int(input())
l=[]
for _ in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
t=l[0][0]
ans=1
for i in range(1,n):
    if t<l[i][0]-l[i][1]:
        ans+=1
        t=l[i][0]
    elif i==n-1 or l[i][0]+l[i][1]<l[i+1][0]:
        ans+=1
        t=l[i][0]+l[i][1]
    else:
        t=l[i][0]
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text]({1DC23ECF-9D1E-4D9D-9A52-CCE5060A932D}.png)




### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：
题目转化：求最少的点。使得所有线段都被覆盖到。这样的点一定是端点，在端点进行更新


代码：

```python
from math import sqrt
t=0
while True:
    n, d = map(int, input().split())
    k=False
    if n==d==0:
        break
    t+=1
    l=[]
    for i in range(n):
        a,b=map(int,input().split())
        if b>d:
            k=True
        else:
            l.append((a-sqrt(d**2-b**2),a+sqrt(d**2-b**2)))
    input()
    if k:
        print(f'Case {t}: -1')
        continue
    l.sort()
    ans=1
    c=l[0][1]
    for i in range(n):
        if c>=l[i][0]:
            c=min(c,l[i][1])
        else:
            ans+=1
            c=l[i][1]
    print(f'Case {t}: {ans}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text]({A1BB6132-6393-484A-800C-B58B21E2D87E}.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
除了玛雅日历，其他的之前就做过了，上个月自学了算法基础与在线实践，所以过得比较顺。最近主要在写单调栈的题目，如护林员盖房子。
区间最大和，也写了一些贪心，dp，如GONEfishing,滑雪等等。




