from math import gcd
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    la=[0]*(n-1)
    for i in range(1,n):
        la[i-1]=l[i]-l[i-1]
    def solve():
        if n==2:
            if la[0]&(la[0]-1)==0:
                return True
        k=la[0]
        for i in range(1,n-2):
             k=gcd(la[i],k)
        if k&(k-1)!=0:
            return False
        return True
    if solve():
        print('Yes')
    else:
        print('No')


