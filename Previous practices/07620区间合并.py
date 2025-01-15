n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
l.sort()
t=True
r=l[0][1]
for i in range(1,n):
    if r<l[i][0]:
        t=False
        break
    else:
        r=max(r,l[i][1])
if t:
    print(l[0][0],r)
else:
    print('no')
