n=int(input())
l=list(map(int,input().split()))
k=0
for i in range(n-1):
    if l[i]<=l[i+1]:
        k+=1
if k==n-1:
    print('YES')
else:
    print('NO')
