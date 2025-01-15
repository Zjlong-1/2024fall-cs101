#深度优先搜索的方法：
l=[list(map(int,input().split())) for _ in range(5)]
k=[(1,0),(0,1),(-1,0),(0,-1)]
v=[[False]*5 for _ in range(5)]
ans=[]
def one(x, y, path):
    if (x, y) == (4, 4):
        ans.append(path[:])
        return
    v[x][y] = True
    path.append((x, y))
    for i, j in k:
        x1, y1 = x + i, y + j
        if 0 <= x1 < 5 and 0 <= y1 < 5 and l[x1][y1] == 0 and not v[x1][y1]:
            one(x1, y1, path)
    path.pop()
    v[x][y] = False
one(0, 0, [])
la=min(ans,key=len)
print(*la,sep='\n')
print((4,4))
#写着写着发现如果是找最短的，有广度优先搜索会更快。因为后者找到的第一个就是最短的，不需要全部列出来（由其一层层拨开的性质所决定）。
#而dfs则要全部枚举出才能得到答案。
#但如果是求所有的话，dfs与bfs时间复杂度一样，dfs空间复杂度会小很多（不断结束，更新）。
from collections import deque
def bfs(maze, start, end):
    rows, cols =5,5
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, [start])])
    visited[start[0]][start[1]] = True
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maze[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)]))
start = (0, 0)
end = (4, 4)
maze=[list(map(int,input().split())) for _ in range(5)]
result = bfs(maze, start, end)
print(*result,sep='\n')

