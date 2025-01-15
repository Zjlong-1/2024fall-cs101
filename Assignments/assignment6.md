# Assignment #6: Recursion and DP

Updated 2201 GMT+8 Oct 29, 2024

2024 fall, Complied by <mark>张俊龙，工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：建立数学模型即可，先将前n-1个数移动到B做中转，再将第N个移动到C，之后重复。



代码：

```python
l=[]
def h(a,b,c,n):
    if n==1:
        l.append(f'{a}->{c}')
        return
    h(a,c,b,n-1)
    l.append(f'{a}->{c}')
    h(b,a,c,n-1)
n=int(input())
h('A','B','C',n)
print(len(l))
for i in l:
    print(i)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text]({6FA0D695-F9E3-404C-9035-526C304F35F9}.png)




### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：
dfs，递归并回溯


代码：

```python
n=int(input())
l=[False]*(n+1)
ans=[]
l1=[]
def p(n,l,ans,l1,t):
    if t==n+1:
        ans.append(l1[:])
    for i in range(1,n+1):
        if not l[i]:
            l1.append(i)
            l[i]=True
            p(n,l,ans,l1,t+1)
            l[i]=False
            l1.pop()
p(n,l,ans,l1,1)
for i in ans:
    print(*i)
```



代码运行截图 ==（至少包含有"Accepted"）==

![alt text]({1E564E5D-2CCE-4BBB-A768-D3C52568F5B2}.png)



### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：
用la指以第I个位置为起点的最长非增数列长度，所以没=每走一步都只要考虑最近一步。


代码：

```python
n=int(input())
l=list(map(int,input().split()))
la=[-1]*n
for i in range(n-1,-1,-1):
    m=1
    for j in range(n-1,i,-1):
        if l[i]>=l[j] and la[j]+1>m:
            m=la[j]+1
    la[i]=m
print(max(la))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text]({97FD20F2-26D2-4EC9-AD45-ED0D762669F1}.png)




### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：标准DP，背包问题。



代码：

```python
n,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for i in range(n):
    l3.append((l1[i],l2[i]))
l3.sort(key=lambda x:x[1])
la=[[0]*(b+1) for _ in range(n)]
for i in range(n):
    for j in range(l3[i][1],b+1):
        la[i][j]=max(la[i-1][j-l3[i][1]]+l3[i][0],la[i-1][j])
print(la[n-1][b])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text]({A2C93BAC-9068-42CB-9CDF-0FA5B2901B61}.png)



### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：对角线用绝对值刻画，并不断标记不可以取的地方，且用一个列表记录当前选取状态。



代码：

```python
l=[]
ans=[-1]*8
def a(ans,r,c):
    for i in range(r):
        if ans[i]==c:
            return False
        if abs(ans[i]-c)==abs(r-i):
            return False
    return True
def s(ans,r):
    if r==8:
        l.append(ans[:])
        return
    for c in range(8):
        if a(ans,r,c):
            ans[r]=c
            s(ans,r+1)
            ans[r]=-1
s(ans,0)
n=int(input())
for i in range(n):
    print(*[x+1 for x in l[int(input())-1]],sep='')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text]({F0E3F041-7D3A-4887-864A-397A9DDF3822}.png)



### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：无限次取使得不需要刻意维护更新数量。DP即可，但要注意用True、False来使得全取满。



代码：

```python
l=list(map(int,input().split()))
l1=l[1:]
l1.sort()
n=l[0]
la=[0]*(n+1)
lb=[False]*(n+1)
lb[0]=True
for i in range(l1[0],n+1):
    for j in l1:
        if i>=j:
            if lb[i-j]:
                la[i]=max(la[i-j]+1,la[i])
                lb[i]=True
print(la[n])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text]({11926F59-D797-4ACA-9635-46E8AFD44686}.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
最近作业做的比较快（之前把dp,dfs,bfs,递归都学了一遍），每日选做也做完了。额外题做了一点，但不多，如矩形覆盖，好人坏人，照亮房间，还做了一点计算概论A的题。




