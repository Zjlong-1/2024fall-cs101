#思路：周围是水或边界就加一，一一遍历即可。
n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
ans=0
l1=[(1,0),(0,1),(0,-1),(-1,0)]
for i in range(n):
    for j in range(m):
        if l[i][j]==1:
            for dx, dy in l1:
                x, y = dx + i, j + dy
                if x < 0 or y < 0 or y >= m or x >= n:
                    ans += 1
                elif l[x][y]==0:
                    ans+=1
print(ans)

