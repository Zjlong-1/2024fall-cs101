from math import sqrt
t=0
while True:
    n, d = map(int, input().split())
    k=False
    if n==d==0:
        break
    t+=1
    l=[]
    for i in range(n):
        a,b=map(int,input().split())
        if b>d:
            k=True
        else:
            l.append((a-sqrt(d**2-b**2),a+sqrt(d**2-b**2)))
    input()
    if k:
        print(f'Case {t}: -1')
        continue
    l.sort()
    ans=1
    c=l[0][1]
    for i in range(n):
        if c>=l[i][0]:
            c=min(c,l[i][1])
        else:
            ans+=1
            c=l[i][1]
    print(f'Case {t}: {ans}')






