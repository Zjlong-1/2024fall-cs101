n=int(input())
for _ in range(n):
    t=int(input())
    l=list(map(int,input().split()))
    l.sort()
    a=0
    b=False
    for k in range((t+1)//2,0,-1):
        if b:
            break
        for j in range(k-1,2*k-1):
            if l[j]>j-k+2:
                break
            if j==2*k-2:
                a = k
                b=True
                break
    print(a)

