n=int(input())
l=[]
for _ in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
t=l[0][0]
ans=1
for i in range(1,n):
    if t<l[i][0]-l[i][1]:
        ans+=1
        t=l[i][0]
    elif i==n-1 or l[i][0]+l[i][1]<l[i+1][0]:
        ans+=1
        t=l[i][0]+l[i][1]
    else:
        t=l[i][0]
print(ans)
#最左边排左边，以此思路不断递推，从简单入手。离谱的是这竟然是在厕所想出来的！