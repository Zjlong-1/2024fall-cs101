def a(i):
    k=1
    while k*(k+1)//2<=i:
        k+=1
    t=i-(k-1)*k//2
    if t==0:
        print(k-1)
    else:
        print(t)
n=int(input())
for _ in range(n):
    a(int(input()))
#不知道哪里错了
def a(i):
    k=1
    while k*(k+1)//2<i:
        k+=1
    t=i-(k-1)*k//2
    print(t)
n=int(input())
for _ in range(n):
    a(int(input()))
#看错题了，是全转化为字符串，不存在大于10 的数
y=''
a=0
b=0
l=[]
for i in range(1,33000):
    y+=str(i)
    a+=len(str(i))
    b+=a
    l.append(b)
n=int(input())
for _ in range(n):
    x=int(input())
    if x==1:
        print(1)
    else:
        for i in range(len(l)):
            if x<=l[i]:
                ans=x-l[i-1]-1
                print(y[ans])
                break
#双指针数据缓存思想