n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
l2=[0]*n
t=0
for i in range(1,n):
    l2[i]=l2[i-1]+l[i-1]
for i in range(n):
    if l2[i]<=l[i]:
        t+=1
print(t)
#这实际上是错误的，还要加上局部的贪心算法
n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
t=0
a=0
for i in range(n):
    if l[i]>=a:
        t+=1
        a+=l[i]
print(t)