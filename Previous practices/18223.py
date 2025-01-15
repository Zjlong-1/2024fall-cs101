n=int(input())
p=0
for i in range(n):
    p=0
    a,b,c,d=map(int,input().split())
    for z in [a,-a]:
        for x in [b,-b]:
            for f in [c,-c]:
                for k in [d,-d]:
                    if z+x+f+k==24:
                        p=1
    if p==1:
        print('YES')
    else:
        print('NO')

