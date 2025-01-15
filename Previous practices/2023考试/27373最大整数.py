#发现规律，谁拍前取决于10**k-1,构造映射
def f(x):
    return int(x)/(10**(len(x))-1)
m=int(input())
n=int(input())
l=list(input().split())
l.sort(key=lambda x:-f(x))
la=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        k=len(l[i-1])
        if k>j:
            la[i][j]=la[i-1][j]
        else:
            la[i][j]=max(la[i-1][j],la[i-1][j-k]*(10**k)+int(l[i-1]))
print(la[-1][-1])