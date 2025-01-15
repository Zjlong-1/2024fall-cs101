n=int(input())
l=[0]+list(map(int,input().split()))
s=[i for i in range(1000002)]
def find(x):
    if x!=s[x]:
        s[x]=find(s[x])
    return s[x]
for i in range(1,n+1):
    k=find(l[i])
    l[i]=k
    s[k]=find(k+1)
print(*l[1:])