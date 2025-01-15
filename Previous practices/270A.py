n=int(input())
l=[]
for t in range(3,361):
    if (t-2)*180%t==0:
        w=(t-2)*180//t
        l.append(w)
for i in range(n):
    a=int(input())
    if a in l:
        print('YES')
    else:
        print('NO')
