s=int(input())
l=[0]*10001
for p in range(2,int(101)):
    if l[p]==0:
        for i in range(p*p,10001,p):
            l[i]=1
k=[p for p in range(2,10001) if l[p]==0]
for j in k:
    if 2*j>=s and s-j in k:
        print(j*(s-j))
        break



