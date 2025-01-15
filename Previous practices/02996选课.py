n=int(input())
m=int(input())
l=list(map(int,input().split()))
for o in range(m):
    t = n - 1
    while l[t] < l[t - 1]:
        t -= 1
        if t == 0:
            l.sort()
            break
    for i in range(n - 1, t - 1, -1):
        if l[i] > l[t - 1]:
            l[t - 1], l[i] = l[i], l[t - 1]
            l[t:] = reversed(l[t:])
            break
print(*l)
#和排列差不多，还更简单