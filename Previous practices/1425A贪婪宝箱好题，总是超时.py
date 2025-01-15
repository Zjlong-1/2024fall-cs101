n=int(input())
for _ in range(n):
    t=int(input())
    ans=0
    while t>0:
        if t%2==0:
            ans+=t//2
            t=t//2
        else:
            ans+=1
            t-=1
        if t>0 and t%2==0:
            t=t//2
        elif t>0 and t%2==1:
            t-=1
    print(ans)
#很简单，但超时了，难受。
#用递归加数据缓存处理尝试一下,好像缓存也没用，应该要用数学公式（10**18，一个数据都过不了）
#不行，就算这样也要尝试（每次至少/2,量级应该可以降下去）
la=[False]*(10**18+1)
lb=[-1]*(10**18+1)
lb[0]=0
la[0]=True
def g(t):
    if la[t]:
        return lb[t]
    la[t]=True
    if t%4==0:
        return g(t//4)+t//2
    if t%4==2:
        return g((t-2)//2)+t//2
    if t%4==1:
        return g((t-1)//2)+1
    if t%4==3:
        return g((t-1)//2)+1
n=int(input())
for _ in range(n):
    t=int(input())
    print(g(t))
#memorry error 太难受了
#事实上，我的算法也有问题，t%4==0时不能取一半，要取一个（是对方取的比较少）。
import sys
data1 = sys.stdin.read
data = data1().split()
t = int(data[0])
numbers = list(map(int, data[1:t + 1]))
ans=[]
for i in numbers:
    a,b=0,1
    while i:
        k=0
        if i%4==2 or i==4:
            i=i//2
            k=i
        else:
            i-=1
            k=1
        if b:
            a+=k
        b^=1
    ans.append(a)
print('\n'.join(map(str,ans)))
#还是超时，要减化MOD
import sys
data1 = sys.stdin.read
data = data1().split()
t = int(data[0])
numbers = list(map(int, data[1:t + 1]))
ans=[]
for i in numbers:
    a,b=0,1
    while i:
        k=0
        if i&3==2or i==4:
            i=i//2
            k=i
        else:
            i-=1
            k=1
        if b:
            a+=k
        b^=1
    ans.append(a)
print('\n'.join(map(str,ans)))
#还是过不了，只能用PYPY了
