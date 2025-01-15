t=int(input())
for _ in range(t):
    n=int(input())
    k=0
    ans=n*(n+1)//2
    while n>=2:
        k+=1
        n=n//2
    ans=ans-(2**(k+1)-1)*2
    print(ans)