n,m=map(int,input().split())
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    for t in range(l[0]):
        a.append(l[t+1])
a=set(a)
if sum(a)==int((m+1)*m/2):
    print('YES')
else:
    print('NO')

