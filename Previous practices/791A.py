n,m=map(int,input().split())
k=0
while n<=m:
    k+=1
    n=n*3
    m=m*2
print(k)