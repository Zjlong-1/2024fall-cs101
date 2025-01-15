def c(l,a,k):
    for i in range(k):
        a=l[a]
    return a
def zhou(l,n):
    lz=[]
    for i in range(n):
        x=l[i]
        t=1
        while x!=i:
            x=l[x]
            t+=1
        lz.append(t)
    return lz
while True:
    n = int(input())
    if n==0:
        break
    l = list(map(int, input().split()))
    for i in range(n):
        l[i]-=1
    lz=zhou(l,n)
    while True:
        l1=input().split(' ',1)
        if l1[0]=='0':
            break
        k=int(l1[0])
        lb=list(l1[1])
        while len(lb)<n:
            lb.append(' ')
        ans=['']*n
        for i in range(n):
            ans[c(l,i,k%lz[i])]=lb[i]
        print(*ans,sep='')
    print()
#思想简单，但实现十分复杂

