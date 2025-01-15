n,m=map(int,input().split())
l=list(map(int,input().split()))
la=[1]*n
s=set()
s.add(l[n-1])
for i in range(n-2,-1,-1):
    if l[i] not in s:
        s.add(l[i])
        la[i]=la[i+1]+1
    else:
        la[i]=la[i+1]
for i in range(m):
    print(la[int(input())-1])
