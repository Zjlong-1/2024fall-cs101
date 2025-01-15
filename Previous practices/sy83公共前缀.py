n=int(input())
l=list(input() for i in range(n))
t=min(len(i) for i in l)
x=[]
for k in range(t):
    a=0
    for i in range(n):
        if l[0][k]!=l[i][k]:
            a=1
    if a==0:
        x.append(l[0][k])
    if a==1:
        break
print(*x,sep='')



