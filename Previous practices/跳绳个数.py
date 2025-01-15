t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    if len(l)==1:
        print(60)
    else:
        s=set(l[1:])
        t=0
        cnt1=0
        cnt2=0
        while t<60:
            if cnt2 not in s:
                cnt1+=1
                cnt2=cnt1
                t+=1
            else:
                t+=3
                cnt2+=1
        print(cnt1)


