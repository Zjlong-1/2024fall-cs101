a,b=map(int,input().split())
l=[]
for i in range(a,b+1):
    q=i//100
    w=(i%100)//10
    e=i%10
    if q**3+w**3+e**3==i:
        l.append(i)
if len(l)==0:
        print('NO')
else:
        print(*l)