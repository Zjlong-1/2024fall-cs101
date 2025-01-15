from bisect import bisect_left
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    la=[]
    for i in range(n):
        la.append((l[2*i],l[2*i+1]))
    la.sort()
    l1=[]
    for i in range(n-1,-1,-1):
        l1.append(la[i][1])
    ans=[]
    for i in l1:
        t=bisect_left(ans,i)
        if t<len(ans):
            ans[t]=i
        else:
            ans.append(i)
    print(len(ans))

