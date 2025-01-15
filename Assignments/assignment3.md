# Assign #3: Oct Mock Exam暨选做题目满百

Updated 1537 GMT+8 Oct 10, 2024

2024 fall, Complied by Hongfei Yan==张俊龙 工学院==



**说明：**

1）Oct⽉考： AC6==（请改为同学的通过数）== 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/



思路：构造两个字符串，一个大写一个小写，再通过条件进行模即可。但要注意字符串不可定义，所以a要是列表。



代码

```python
k=int(input())
a=[i for i in input()]
l='abcdefghijklmnopqrstuvwxyz'
l1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(a)):
    for j in range(26):
        if l[j]==a[i]:
            a[i]=l[(j-k)%26]
            break
        if  l1[j]==a[i]:
            a[i]=l1[(j-k)%26]
            break
print(*a,sep='')
```



代码运行截图 ==（至少包含有"Accepted"）==

![alt text]({9329E0BC-09F2-4068-BC85-CE102A576792}.png)



### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/



思路：去切片，转整数再求和。



代码

```python


```a,b=input().split()
a=a[0:2]
b=b[0:2]
print(int(a)+int(b))



代码运行截图 ==（至少包含有"Accepted"）==
![alt text]({77B3AEB5-E2CF-478E-89CD-B432E423E55A}.png)





### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/



思路：按题目来一一计算，最后在进行判断。



代码

```python
n=int(input())
l=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
l1=[1,0,'X',9,8,7,6,5,4,3,2]
for i in range(n):
    a=input()
    t=0
    for j in range(17):
        t+=int(a[j])*l[j]
    t=t%11
    if str(l1[t])==a[-1]:
        print('YES')
    else:
        print('NO')


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text]({C991C762-6871-49A7-B9A0-CAF4841F4CCB}.png)



### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/



思路：用while进行多次操作直至结束。



代码

```python
n=int(input())
while n!=1:
    if n%2==0:
        n=n//2
        print('{}/2={}'.format(2*n,n))
    else:
        print('{}*3+1={}'.format(n,n*3+1))
        n = n * 3 + 1
print('End')

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/



思路：将一些特殊的情况作为单独的数的运算单位。罗马数字转整数时，小在右是减，大在左是加。



##### 代码

```python
 n=input()
l1=['1','2','3','4','5','6','7','8','9','0']
l2=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
l=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
l3=[]
l4= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
if n[0] in l1:
    n=int(n)
    for i in range(13):
        t=n//l2[i]
        n=n%l2[i]
        l3.append(l[i]*t)
    print(*l3,sep='')
else:
    t=0
    ans=0
    for i in reversed(n):
        k=l4[i]
        if k<t:
            ans-=k
        else:
            ans+=k
        t=k
    print(ans)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text]({EC54AC01-9384-4613-93A2-9B5601924218}.png)



### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/



思路：要尽可能使第1个最小，再第2个最大。而X可以到第1个，那么会经过X-1到1，这要求与这些数都是可交换的，这样只需递推上下界，并卡在d的零域上。
转化为多次局部最优



代码

```python
l1=[False]*n
a=[]
while False in l1:
    i=0
    k=[]
    while i<n:
        if l1[i]:
            i+=1
            continue
        if len(k)==0:
            k.append(l[i])
            maxz=l[i]
            minz=l[i]
            l1[i] = True
            i+=1
            continue
        maxz=max(maxz,l[i])
        minz=min(minz,l[i])
        if maxz-l[i]<=d and l[i]-minz<=d:
            k.append(l[i])
            l1[i]=True
        i+=1
    k.sort()
    a.extend(k)
print(*a,sep='\n')

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text]({147381A9-E919-4D1D-80B6-A11F2D13CC7D}.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

考试时最后一题没做出来，也没什么明显思路。考后思考发现是自己考试由于只关注题干表面，未将题目进行转化导致的。
所以在之后我看了算法的书，也学习了一些算法，如递归，动态规划，深度优先搜索等等。写了黑皇后，汉诺塔，假币问题等等。希望下次可以攻破最后一题。










