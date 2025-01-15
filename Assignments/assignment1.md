# Assignment #1: 自主学习

Updated 0110 GMT+8 Sep 10, 2024

2024 fall, Complied by ==张俊龙，工学院=



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/



思路：把一些特殊情况列举出来，再用else即可



##### 代码

```python
# a=int(input())
if a%100==0 and a%400!=0:

    print('N')
elif a%3200==0:
    print('N')
elif a%4!=0:
    print('N')
else:
    print('Y')

```



代码运行截图 ==（至少包含有"Accepted"）==

![alt text](IMG_20240920_113303.jpg)



### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/



思路：模4分类



##### 代码

```python
# a=int(input())
if a%4==0:
    print(int(a/4),int(a/2))
elif a%4==1:
    print(0,0)
elif a%4==3:
    print(0,0)
else:
     print(int(a/4+1),int(a/2))

```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text](IMG_20240920_113303-1.jpg)




### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：事实上，有偶数列或行时显然可以放满。而奇数时可以拆成偶数加一，至多空一个。综上即为行列相乘取下整。



##### 代码

```python
# a,b=map(int,input().split())
print(int (a*b/2))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==
![alt text](IMG_20240920_114136.jpg)





### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：行与列相互独立，除后取上整再相乘



##### 代码

```python
# import math
a,b,c=map(int,input().split())
n=math.ceil(a/c)
m=math.ceil(b/c)
print(n*m)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==
![alt text](IMG_20240920_114937.jpg)




### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：字符串可以比大小！



##### 代码

```python
# a=input().lower()
b=input().lower()
n=0
for i in range(len(a)):
    if ord(a[i])>ord(b[i]):
        print(1)
        break
    elif ord(a[i])<ord(b[i]):
        print(-1)
        break
    else :n+=1
if n==len(a):
    print(0)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==
![alt text](IMG_20240920_115011.jpg)




### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：数1的个数即可（用加法来数1）



##### 代码

```python
# a=int(input())
n=0
for i in range(a):
    m=map(int,input().split())
    b=sum(m)
    if b>1:
        n+=1
    else:
        n=n
print(n)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==
![alt text](IMG_20240920_115031.jpg)




## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==
做了一下OJ“计概2024fall每日选做”




