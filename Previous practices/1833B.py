n=int(input())
for i in range(n):
    m,k=map(int,input().split())
    a=list(map(int,input().split()))
    v=[(a[g],g)for g in range (m)]
    b=list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    v.sort()
    for t in range(m):
        for o in range(t,m):
            if abs(a[t]-b[o])<=k:
                b[o],b[t]=b[t],b[o]
                break
    z=[0]*m
    for u in range (m):
        z[v[u][1]]=b[u]
    print(*z)#又麻烦又有错误
    #还是参考别人吧

t = int(input())
for _ in range(t):
    j, k = map(int, input().split())

    l1 = list(map(int, input().split()))
    v = [(l1[i], i) for i in range(j)]
    v.sort()

    l2 = list(map(int, input().split()))
    l2.sort()

    z = [0] * j
    for i in range(j):
        z[v[i][1]] = l2[i]

    for data in z:
        print(data, end=" ")
    print()

