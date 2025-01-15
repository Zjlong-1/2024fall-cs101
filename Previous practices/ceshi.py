t=0
l=[]
for a in range(2,10**6):
    for k in range(2, int(a ** 0.5) + 1):
        if a % k == 0:
            t = 2
    if t==0:
        l.append(a**2)
n=int(input())
p=list(map(int,input().split()))
for i in p:
    if i in l:
        print('YES')
    else:
        print('NO')
#又超时了




