n=int(input())
for _ in range(n):
    a,b=input().split()
    l=[]
    for i in range(len(a)):
        l.append((int(a[i]),i))
    l.sort(key=lambda x:(-x[0],x[1]))
    l1=l[int(b):]
    l1.sort(key=lambda x:x[1])
    print(''.join(str(i[0]) for i in l1))
#算法逻辑错误：4199999 1就会出问题
#事实上，首位数要先最小，即考虑前k个数并取其中最小值。再依次下去。但又有问题了，因为有两个数都取得最小值时，无法判断要哪一个。
#所以这个解法还是有漏洞
n=int(input())
for _ in range(n):
    a,b=input().split()
    l=[int(i) for i in a]
    l1=l[:int(b)+1]
    t=l1[0]
    for i in range(1,int(b)+1):
        if t<
#但再次细想若两个相邻，都不动，不相邻时不必纠结两者生存情况，事实上都留下，把中间去掉才是最优解。

from collections import deque
n=int(input())
for _ in range(n):
    a,b=input().split()
    q=deque()
    k=int(b)
    for i in a:
        while q and k > 0 and int(i)<q[-1]:
            q.pop()
            k-=1
        q.append(int(i))
    while k>0:
        q.pop()
        k-=1
    print(*q,sep='')


