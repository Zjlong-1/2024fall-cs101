n=int(input())
for i in range(n):
    m=int(input())
    k=0
    t=0
    while m%3==0:
        k+=1
        m=m//3
    while m%2==0:
        t+=1
        m=m//2
    if m!=1 or t>k:
        print(-1)
    else:
        print(k-t+k)

