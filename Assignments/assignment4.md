# Assignment #4: T-primes + 贪心

Updated 0337 GMT+8 Oct 15, 2024

2024 fall, Complied by <mark>张俊龙 工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：
只取小于0的是，用if判断即可


代码

```python
# n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
k=0
g=0
for i in l:
    if i<=0:
        k+=1
if k>=m:
    print(-sum(l[0:m]))
else:
    for h in l:
        if h<=0:
            g=h+g
    print(-g)


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text]({D417D794-F128-4531-8BC9-C58B684C7B47}.png)



### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A

思路：从大到小依次加，直到超过一半。



代码

```python
n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
t=0
k=0
for i in range(n):
    if t*2>sum(l):
        break
    else :
        t+=l[i]
        k=i+1
print(k)

```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text]({7C71249A-18A8-4024-8362-043649469F57}.png)




### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B

思路：
行和或列和是固定的，剩余的取最小的即可。


代码

```python
n=int(input())
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(min(sum(a)+m*min(b),sum(b)+m*min(a)))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text]({647DD11E-9EA5-42AD-B610-949848B47407}.png)



### 158B. Taxi

*special problem, greedy, implementation, 1100, https://codeforces.com/problemset/problem/158/B

思路：和装箱问题思路一样，先确定必须的箱子，再进行填充，看是否要额外的箱子。



代码

```python
from math import(ceil)
n=int(input())
l=list(map(int,input().split()))
t=l.count(4)+l.count(3)+ceil(l.count(2)/2)
k1=l.count(3)+2*(l.count(2)%2)
if l.count(1)>k1:
    print(t+ceil((l.count(1)-k1)/4))
else:
    print(t)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text]({F6C572CD-1FB7-47C0-B8CF-30822D97FE06}.png)




### *230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：

用筛法确定素数，同时将素数附上特殊的值，由于有索引就会快，直接判断索引的值是否等于即可（比盲目地用 in快很多）

代码

```python
l=[0]*1000001
l[0]=l[1]=1
for i in  range(2,1001):
    if l[i]==0:
        for k in range(i*i,1000001,i):
            l[k]=1
n=int(input())
p=list(map(int,input().split()))
for i in p:
    if  int(i**0.5)**2==i:
        a=int(i**0.5)
        if l[a]==0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text]({3C5C4932-3702-4B79-A736-8F6F44F56993}.png)



### *12559: 最大最小整数 （选做）

greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559

思路：比较字典序，想到补全位数，但发现很难做到，于是考虑除以10的I次方量级的数来统一比较，最后推导得出10*i-1即可。



代码

```python
n=int(input())
l=input().split()
l1=[]
for i in range(n):
    l1.append((int(l[i])/(10**len(l[i])-1),i))
l1.sort()
l2=sorted(l1,reverse=True)
a=''.join(l[i] for _ , i in l1)
b=''.join(l[i] for _,i in l2)
print(b+' '+a)


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text]({CF9C28B4-7C23-4A39-AE10-9E5688FBE9F7}.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

作业题目难度还在可控范围内，最近在学习背包九讲，发现动态规划还是挺难的（一开始想不到），此外还学习了单调对列方法。



