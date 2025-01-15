n=int(input())
l=[]
for i in range(n):
    x,y,z=map(int,input().split())
    l.append((x,y,z))
a=abs(sum(l[k][0] for k in range(n) ))
b = abs(sum(l[k][1] for k in range(n)))
c =abs(sum(l[k][2] for k in range(n) ))
if (a+b+c)==0:
    print('YES')
else:
    print('NO')