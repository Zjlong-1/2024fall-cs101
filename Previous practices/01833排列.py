n=int(input())
for _ in range(n):
    m,k=map(int,input().split())
    l=list(map(int,input().split()))
    while k>0:
        t=m-1
        q=[l[t]]
        while l[t]<l[t-1]:
            q.append(l[t-1])
            t-=1
            if t==0:
                k-=1
                l=[i for i in range(1,m+1)]
                break
        q.sort()
        for i in range(len(q)):
            if q[i] > l[t - 1]:
                l[t - 1], q[i] = q[i], l[t - 1]
                l[t:] = q
                k -= 1
                break
    print(*l)
#一次次操作（次数少，不需要快算法）
#有点尴尬，超时了。改进一下，避免多次排序（利用后面部分单调递减的性质，且规避死循环）
n=int(input())
for _ in range(n):
    m,k=map(int,input().split())
    l=list(map(int,input().split()))
    for o in range(k):
        t=m-1
        while l[t]<l[t-1]:
            t-=1
            if t==0:
                l.sort()
                break
        for i in range(m-1,t-1,-1):
            if l[i] > l[t - 1]:
                l[t - 1], l[i] = l[i], l[t - 1]
                l[t:] = reversed(l[t:])
                break
    print(*l)