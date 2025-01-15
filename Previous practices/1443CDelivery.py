t=int(input())
for _ in range(t):
    n=int(input())
    la=list(map(int,input().split()))
    lb=list(map(int,input().split()))
    l=[]
    for i in range(n):
        l.append((la[i],lb[i]))
    l.sort()
    s=[0]*(n+1)
    l.insert(0,(0,0))
    for i in range(1,n+1):
        s[i]+=s[i-1]+l[i][1]
    print(min(max(s[n]-s[i],l[i][0]) for i in range(n+1)))

