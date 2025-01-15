def a(i,j):
    if l1[i-1][j-1]!=-1:
        return l1[i-1][j-1]
    if i==n:
        l1[i-1][j-1]=l[i-1][j-1]
        return l1[i-1][j-1]
    else:
        l1[i-1][j-1]=max(a(i+1,j),a(i+1,j+1))+l[i-1][j-1]
        return l1[i-1][j-1]
n=int(input())
l=[[int(i) for i in input().split()] for i in range(n)]
l1=[[-1 for _ in range(n)] for i in range(n)]
print(a(1,1))

    