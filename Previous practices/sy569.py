n,q=map(int,input().split())
l1=[]
l2=[]
t=0
for i in range(q):
    a,b=map(int,input().split())
    l1.append((a,b))
    l2.append((b,a))
for i in l1:
    if i in l2:
        t=1
if t==1:
    print('Yes')
else:
    print('No')