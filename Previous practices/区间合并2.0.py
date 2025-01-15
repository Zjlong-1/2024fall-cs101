n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
l.sort()
t=True
r=l[0][1]
ans=[]
for i in range(1,n):
    if r<l[i][0]:
        t=False
        ans.append((l[i][0]+1-r,r,l[i][0]))
    r=max(r,l[i][1])
if t:
    print('Not Needed')
else:
    ans.sort()
    for a,b,c in ans:
        print(b,c)
