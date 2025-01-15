t=int(input())
for _ in range(t):
    n,m,x,y=map(int,input().split())
    k=m*n
    l=[[False]*m for i in range(n)]
    l1=[(1,2),(1,-2),(-1,-2),(-1,2),(2,1),(2,-1),(-2,1),(-2,-1)]
    ans=0
    def dfs(x,y,step):
        global ans
        if step==k:
            ans+=1
        for dx,dy in l1:
            nx,ny=dx+x,dy+y
            if 0<=nx<n and 0<=ny<m and not l[nx][ny]:
                l[nx][ny]=True
                dfs(nx,ny,step+1)
                l[nx][ny]=False
    l[x][y]=True
    dfs(x,y,1)
    print(ans)
