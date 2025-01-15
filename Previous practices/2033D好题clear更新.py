t = int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int, input().split()))
    la=set()
    k=0
    ans= 0
    for i in l:
        k+=i
        if k== 0 or k in la:
            ans += 1
            k = 0
            la.clear()
        else:
            la.add(k)
    print(ans)