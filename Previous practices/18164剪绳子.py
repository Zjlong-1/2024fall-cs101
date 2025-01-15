#一共剪n-1刀，先将最大的剪掉（省的一直贡献极大的长度）,z这是对的，但不知道是减去一个还是减去多个
n=int(input())
l=list(map(int,input().split()))
ans=0
s=0
l.sort()
for j in l:
    s+=j
    ans+=s
print(ans-l[0])
#好吧，我的思路其实有问题，因为这样还会使前缀和一直做贡献，使得结果偏大。
#要从中间切开,本质上就是实现树的结构，没有见过基本上是写不出来的
def solve(t,s):
    k=sum(s)
    cs=0
    for i in range(t):
        cs+=s[i]
        if cs>=k/2:
#从反的方向考虑会好很多，即把n个拼起来，这只要处理两个最小的再将合体加进去化为n-1的情况
import bisect
n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
ans=0
for i in range(n-1):
    a=l.pop()
    b=l.pop()
    ans+=a+b
    bisect.insort(l,a+b)
print(ans)
#又被坑了，OJ上面单调递增的数列不能用BISECT
#所以要加负号处理

import bisect
n=int(input())
l=sorted(list(map(lambda x:-int(x),input().split())))
ans=0
for i in range(n-1):
    a=l.pop()
    b=l.pop()
    ans-=a+b
    bisect.insort(l,a+b)
print(ans)
#用堆来实现会快一点：
import heapq

n = int(input())  # 读取第一个输入，表示数据的数量
a = list(map(int, input().split()))  # 读取一行输入，转化为整数列表
heapq.heapify(a)  # 将列表转换为一个最小堆
ans = 0

# 进行 n-1 次合并操作
for i in range(n-1):
    x = heapq.heappop(a)  # 弹出最小的元素
    y = heapq.heappop(a)  # 再弹出最小的元素
    z = x + y  # 合并这两个元素
    heapq.heappush(a, z)  # 将合并后的结果重新插入堆中
    ans += z  # 将合并代价加到总答案中

print(ans)  # 输出最终结果
