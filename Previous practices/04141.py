a1,a2,a3,a4,a5,a6=map(int,input().split())
l=[]
for a in range(a1+1):
    for b in range(a2+1):
        for c in range(a3+1):
            for d in range(a4+1):
                for e in range(a5+1):
                    for f in range(a6+1):
                        l.append(a+2*b+3*c+5*d+10*e+20*f)
l=set(l)
print('Total={}'.format(len(l)-1))

