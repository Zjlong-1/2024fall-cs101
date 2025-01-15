t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l=[list(input()) for i in range(n)]
    l1=[(0,1),(0,-1),(1,1),(1,0),(1,-1),(-1,0),(-1,-1),(-1,1)]
    def dfs(x,y):
        global cnt
        cnt += 1
        for dx,dy in l1:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and l[nx][ny]=='W':
                l[nx][ny]='.'
                dfs(nx,ny)
    ans=0
    for i in range(n):
        for j in range(m):
            if l[i][j]=='W':
                l[i][j]='.'
                cnt=0
                dfs(i,j)
                ans=max(ans,cnt)
    print(ans)
#dfs 还是要从最简单的情形来找思路，切中突破点。多练！！！！！！