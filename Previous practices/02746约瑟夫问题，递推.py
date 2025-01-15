def a(n,m):
    t=1
    for i in range(2,n+1):
        t=(t+m)%i
    print(t)
while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    a(n,m)
#这里有bug ,即第n个变成了第0个，不妨转换一下思路，将所有次序都减一，模完之后再加上1.这样就可以实现了
def a(n,m):
    t=0
    for i in range(2,n+1):
        t=(t+m)%i
    print(t+1)
while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    a(n,m)