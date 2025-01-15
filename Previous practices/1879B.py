n=int(input())
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(min(sum(a)+m*min(b),sum(b)+m*min(a)))
