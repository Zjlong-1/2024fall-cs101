# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by <mark>张俊龙，工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：周围是水或边界就加一，一一遍历即可



代码：

```python
n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
ans=0
l1=[(1,0),(0,1),(0,-1),(-1,0)]
for i in range(n):
    for j in range(m):
        if l[i][j]==1:
            for dx, dy in l1:
                x, y = dx + i, j + dy
                if x < 0 or y < 0 or y >= m or x >= n:
                    ans += 1
                elif l[x][y]==0:
                    ans+=1
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：用数字记录走的方向，不断判断是否可以按照原方向走下去，如果不行则装90度继续走



代码：

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        i,j=0,0
        k=1
        l=[[True]*m for _ in range(n)]
        la=[matrix[i][j]]
        l[0][0]=False
        count=1
        while True:
            if count==m*n:
                break
            if k==1 :
                if j+1<m and l[i][j+1]:
                    j+=1
                    la.append(matrix[i][j])
                    l[i][j]=False
                    count+=1
                else:
                    k=2
            elif k==2:
                if i+1<n and l[i+1][j]:
                    i+=1
                    la.append(matrix[i][j])
                    l[i][j] = False
                    count += 1
                else:
                    k=3
            elif k==3:
                if j-1>=0 and l[i][j-1]:
                    j-=1
                    la.append(matrix[i][j])
                    l[i][j] = False
                    count += 1
                else:
                    k=4
            elif k==4:
                if i-1>=0 and l[i-1][j]:
                    i-=1
                    la.append(matrix[i][j])
                    l[i][j] = False
                    count += 1
                else:
                    k=1
        return la 
```



代码运行截图 ==（至少包含有"Accepted"）==

![alt text](image-1.png)



### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：好坑：区间在0到1024之间！



代码：

```python
l=[[0]*1025 for i in range(1025)]
d=int(input())
for _ in range(int(input())):
    x,y,i=map(int,input().split())
    for k in range(max(x-d,0),min(x+d+1,1025)):
        for j in range(max(y-d,0),min(y+d+1,1025)):
            l[k][j]+=i
t=-1
for i in l:
    for j in i:
        if j>t:
            a=1
            t=j
        elif j==t:
            a+=1
print(str(a)+' '+str(t))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-2.png)



### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：贪心即可，每次取最有利于下一项的数。但要注意把前面全相等的情况用while循环弄掉。



代码：

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        k=nums[0]
        ans=1
        h=1
        while nums[h]==k:
            h+=1
            if h==len(nums):
                return 1
        if nums[0]>nums[h]:
            t=True
            ans+=1
        else:
            t = False
            ans+=1
        k=nums[h]
        for i in range(h+1,len(nums)):
            if t:
                if nums[i]>k:
                    ans+=1
                    t=False
            else:
                if nums[i]<k:
                    ans+=1
                    t=True
            k=nums[i]
        return ans 
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：前面i个（不在乎第i个的状态）最大的可能



代码：

```python
from collections import Counter
n=int(input())
l=list(map(int,input().split()))
s=Counter(l)
s=sorted(s.items())
la=[0]*(len(s)+1)
la[1]=s[0][0]*s[0][1]
for i in range(2,len(s)+1):
    if s[i-1][0]==s[i-2][0]+1:
        la[i]=max(la[i-1],la[i-2]+s[i-1][1]*s[i-1][0])
    else:
        la[i]=la[i-1]+s[i-1][1]*s[i-1][0]
print(la[len(s)])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-4.png)




### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：考虑收尾来减少马数的贪心算法。



代码：

```python
while True:
    n=int(input())
    if n==0:
        break
    t=0
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l1.sort()
    l2.sort()
    k1=n-1
    k2=n-1
    s1,s2=0,0
    while s1<=k1 and s2<=k2:
        if l1[k1] > l2[k2]:
            t += 200
            k1 -= 1
            k2 -= 1
        elif l1[k1] < l2[k2]:
            t -= 200
            k2 -= 1
            s1 += 1
        else:
            if l1[s1] > l2[s2]:
                t += 200
                s1 += 1
                s2 += 1
            else:
                if l1[s1]<l2[k2]:
                    s1 += 1
                    k2 -= 1
                    t -= 200
                else:
                    s1 += 1
                    k2 -= 1
    print(t)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
田忌赛马之前了解过算法思想，所以还是比较顺。期中考考完了，最近把每日选做补上了。在加强对栈，双指针的理解，做了leetcode上的100题。最近还学了并查集+路径压缩。




