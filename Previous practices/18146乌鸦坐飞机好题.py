#看错题了，被图误导了,三个和一个时都要浪费一个
from math import ceil
n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
t4,t2=n,n*2
l1=[]
for j in l:
    while j>=4 and t4>0:
        j-=4
        t4-=1
    l1.append(j)
l1.sort(reverse=True)
t=0
if t4>0:
    for j in range(len(l1)):
        if l1[j]!=3 or t4==0:
            break
        t=j
        t4-=1
    t1=len(l1)-1
    for i in range(len(l1)-1,t):
        if l1[i]>1 or t4==0:
            break
        t1=i
        t4-=1
        t2+=1
    t2+=t4
    for i in range(t+1,t1):
        t2-=ceil(l1[i]/2)
else:
    for j in l1:
        t2-=ceil(j/2)
if t2<0:
    print('NO')
else:
    print('YES')

#缝缝补补过不了（2+2+2=（2+1）+（1+2）这个情况没有考虑到，而且这种情况只能用空位来做），干脆换一种写法：（模4考虑）



n, _ = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0]*4
for i in a:
    cnt[i % 4] += 1
# add为空位数
add = cnt[1]+cnt[3]  # 余1或3的必定会造成一个空位
# 余2的优先放1、2和7、8，或和余1的组合放中间，不会增加空位数
t = cnt[2]-2*n-cnt[1]
if t > 0:  # 若还有余2的没能放好
    # 分类讨论余2的至少造成多少个空位
    add += t//3*2
    if t % 3 == 1:
        add += 2
    if t % 3 == 2:
        add += 4
print('YES' if sum(a)+add <= n*8 else 'NO')