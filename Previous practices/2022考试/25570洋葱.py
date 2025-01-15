n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
def solve(x):
    k=0
    for i in range(x,n-x):
        k+=l[i][x]+l[i][n-1-x]
    for i in range(x+1,n-1-x):
        k+=l[x][i]+l[n-1-x][i]
    return k
if n%2==0:
    print(max(solve(i) for i in range(n//2)))
elif n==1:
    print(l[0][0])
else:
    ans=max(solve(i) for i in range(n//2))
    print(max(ans,l[n//2][n//2]))