n=int(input())
l=[False]*(n+1)
ans=[]
l1=[]
def p(n,l,ans,l1,t):
    if t==n+1:
        ans.append(l1[:])
    for i in range(1,n+1):
        if not l[i]:
            l1.append(i)
            l[i]=True
            p(n,l,ans,l1,t+1)
            l[i]=False
            l1.pop()
p(n,l,ans,l1,1)
for i in ans:
    print(*i)

