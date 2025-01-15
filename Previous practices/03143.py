x=int(input())
t=[]
a=[]
if x<6 or x%2==1:
    print('Error!')
else:
    for i in range(2,x):
        l=[]
        for s in range(2,i):
            if i%s==0:
                l.append(i)
        if len(l)==0:
            t.append(i)
for j in t:
    for u in t:
        if j+u==x:
            a.append((min(j,u),str(x)+'='+str(min(j,u))+'+'+str(max(j,u))))
a=list(set(a))
a.sort()
o=[]
for i in range(len(a)):
    o.append(a[i][1])
print(*o,sep='\n')
#可以改进：
x=int(input())
t=[]
a=[]
if x<6 or x%2==1:
    print('Error!')
else:
    for i in range(2,x):
        l=[]
        for s in range(2,i):
            if i%s==0:
                l.append(i)
        if len(l)==0:
            t.append(i)
for j in t:
    if j>x/2:
        break
    if x-j in t:
        a.append((j,str(x)+'='+str(j)+'+'+str(x-j)))
a.sort()
a=list(set(a))
o=[]
for i in range(len(a)):
    o.append(a[i][1])
print(*o,sep='\n')







