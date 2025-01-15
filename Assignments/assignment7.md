# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>张俊龙 工学院</mark>



**说明：**

1）⽉考： AC6<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：直接划分两个集合，分别装两种病人。



代码：

```python
n=int(input())
l1=[]
l2=[]
for i in range(n):
    a,b=input().split()
    b=int(b)
    if b>=60:
        l1.append((a,b,i))
    else:
        l2.append((a,b,i))
l1.sort(key=lambda x:(-x[1],x[2]))
for i in l1:
    print(i[0])
for i in l2:
    print(i[0])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：先转化为正常矩阵，在进行运算，最后转换回来。



代码：

```python
n,m1,m2=map(int,input().split())
l1=[[0]*n for _ in range(n)]
l2=[[0]*n for _ in range(n)]
l=[[0]*n for _ in range(n)]
for i in range(m1):
    a,b,c=map(int,input().split())
    l1[a][b]=c
for i in range(m2):
    a,b,c=map(int,input().split())
    l2[a][b]=c
for i in range(n):
    for j in range(n):
        for k in range(n):
            l[i][j]+=l1[i][k]*l2[k][j]
for i in range(n):
    for j in range(n):
        if l[i][j]!=0:
            print(i,j,l[i][j])
```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text](image-3.png)




### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：这个题就是要把最大伤害的打出去，但判断是否有m个可以打还需要循环，比较繁琐。



代码：

```python
t=int(input())
for _ in range(t):
    n,m,b=map(int,input().split())
    l=[]
    for i in range(n):
        a,c=map(int,input().split())
        l.append((a,c))
    l.sort(key=lambda x:(x[0],-x[1]))
    x = l[-1][0]
    k=1
    now=l[0][0]
    for i in range(n):
        if k<=m and l[i][0]==now:
            b-=l[i][1]
            k+=1
        elif l[i][0]!=now:
            k=2
            b-=l[i][1]
            now=l[i][0]
        if b<=0:
            print(now)
            break
    if b > 0:
        print('alive')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)




### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：
完全背包，考虑前I个兑换的最小数，以此进行递推。考试时一直超时，感觉思路也没什么问题，卡了很久。结果发现多了一个判断，要把if 判断语句删除才能过。


代码：

```python
n, m = map(int, input().split())
l = list(map(int, input().split()))
la = [float('inf')] * (m + 1)
la[0] = 0
for i in range(n):
    for j in range(l[i], m + 1):
        la[j] = min(la[j], la[j - l[i]] + 1)
print(la[m] if la[m] != float('inf') else -1)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：小余1000的直接计算，大于1000的要先算系数在乘上倍数。



代码：

```python
s={'negative':-1, 'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12,'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90, 'hundred':100, 'thousand':1000, 'million':1000000}
l=input().split()
if l[0]=='negative':
    l=l[1:]
    t=True
else:
    t=False
ans=0
c=0
for i in l:
    a=s[i]
    if a==100:
        c*=a
    elif a==1000 or a==1000000:
        c*=a
        ans+=c
        c=0
    else:
        c+=a
ans+=c
if t:
    print((-1)*ans)
else:
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-2.png)



### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：
就是包装了的区间合并文题


代码：

```python
n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
l.sort(key=lambda x:x[0])
la=[1]*n
for i in range(n):
    for j in range(i):
        if l[i][0]>l[j][1]:
            la[i]=max(la[j]+1,la[i])
print(max(la))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
这次考试被找零问题卡了，思路是比较明显的，但敲完代码后一直超时，所以有点搞心态，一直死磕，导致最后一题看都没看（考后4分钟就ac了）这说明考试的策略还是比较重要的，可以先跳过全做完了之后再回头看。考后发现找零问题在最后用了if判断，这导致了超时，去掉就过了，还是考试太急了，多写了一个判断。考试后把代码写成函数形式，发现有快了不少，以后超时不严重的话可以考虑转化为函数，可能可以过。总体感觉难度并不算大，但一定要注意考试心态与策略。




