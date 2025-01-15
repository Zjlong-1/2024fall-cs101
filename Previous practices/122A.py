n=int(input())
l=[4,7,44,47,77,74]
k=[4,7]
for i in k:
    for t in k:
        for p in k:
            l.append(i*100+t*10+p)
a=0
for i in l:
    if n%i==0:
        a=1
if a==1:
    print('YES')
else:
    print('NO')
