n,m=map(int,input().split())
ins=set()
s=[i for i in range(1+n)]
def f(x):
    if x!=s[x]:
        s[x]=f(s[x])
    return s[x]
ans=0
for i in range(m):
    a,b=map(int,input().split())
    x,y=f(a),f(b)
    if x!=y:
        s[x]=y
for i in range(1,1+n):
    if f(i) not in ins:
        ans+=1
        ins.add(f(i))
print(ans)