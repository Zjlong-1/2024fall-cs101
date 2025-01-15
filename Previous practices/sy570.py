n,q=map(int,input().split())
l=[]
h=0
for _ in range(q):
    a,b=map(int,input().split())
    l.append((a,b))
for i in l:
    for j in l:
        for k in l:
            if i[1]==j[0] and i[0]==k[1] and k[0]==j[1]:
                h=1
if h==1:
    print('Yes')
else:
    print('No')

