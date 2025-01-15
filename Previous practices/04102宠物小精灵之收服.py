#二维背包问题，思路就是降维，固定其中一个，另一个进行遍历.(前t个时）收服i个（不是第i个，省空间而隐去）的情况下并且只剩j体力的球最大数
#实际上要3维的表，但为了简化和省空间，每次倒着来，在原有的基础上更新。
n,m,k=map(int,input().split())
la=[[-1]*(m+1) for _ in range(k+1)]
la[0][m]=n
for q in range(1,k+1):
    a,b=map(int,input().split())
    for j in range(m+1):
        for i in range(q,0,-1):
            if j+b<=m and la[i-1][j+b]!=-1:
               la[i][j]=max(la[i-1][j+b]-a,la[i][j])
def solve():
    for i in range(k, -1, -1):
        for j in range(m, -1, -1):
            if la[i][j] != -1:
                print(i,j)
                return
solve()

