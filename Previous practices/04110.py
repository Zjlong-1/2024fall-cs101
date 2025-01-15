n,w=map(int,input().split())
p=[]
t=0
for i in range(n):
    a,b=map(int,input().split())
    p.append((float(a/b),a,b))
p.sort(reverse=True)
for i in range(n):
    if p[i][2]<=w:
        w-=p[i][2]
        t+=p[i][1]
    else:
        t+=w*p[i][0]
        w=0
print(f"{t:.1f}")

