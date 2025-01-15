n=int(input())
l=list(map(int,input().split()))
la=[0]*n
if l[0]==0:
    la[0]=1
t=1
while t<n:
    if l[t]==0:
        la[t]=1
        t+=1
        continue
    if l[t]!=3 and l[t]==l[t-1]:
        l[t]=0
        la[t]=1
        t+=1
        continue
    if l[t]==3 and l[t-1]!=3:
        l[t]=3-l[t-1]
    t+=1
print(sum(la))
