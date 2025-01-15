while True:
    n=int(input())
    if n==0:
        break
    t=0
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l1.sort()
    l2.sort()
    k1=n-1
    k2=n-1
    s1,s2=0,0
    while s1<=k1 and s2<=k2:
        if l1[k1] > l2[k2]:
            t += 200
            k1 -= 1
            k2 -= 1
        elif l1[k1] < l2[k2]:
            t -= 200
            k2 -= 1
            s1 += 1
        else:
            if l1[s1] > l2[s2]:
                t += 200
                s1 += 1
                s2 += 1
            else:
                if l1[s1]<l2[k2]:
                    s1 += 1
                    k2 -= 1
                    t -= 200
                else:
                    s1 += 1
                    k2 -= 1
    print(t)


