k1=int(input())
for _ in range(k1):
    n=int(input())
    l=[input() for i in range(n)]
    la=[[0]*n for i in range(n)]
    l1=[(0,1),(1,0),(-1,0),(0,-1)]
    tr=0
    tb=0
    def f(i, j,x,t):
        for a,b in l1:
            ai=a+i
            bj=b+j
            if 0<=ai<=n-1 and 0<=bj<=n-1 and  la[ai][bj]==0 and l[ai][bj]==x:
                la[ai][bj]=t
        return
    for i in range(n):
        for j in range(n):
            if  la[i][j]==0 and l[i][j]=='r':
                k=False
                for a, b in l1:
                    ai=a+i
                    bj=b+j
                    if 0 <= ai <= n - 1 and 0 <= bj <= n - 1 and la[ai][bj]!=0 and l[ai][bj] == 'r':
                        la[i][j] = la[ai][bj]
                        k=True
                        break
                if not k:
                    tr+=1
                    la[i][j]=tr
            if la[i][j]==0 and l[i][j]=='b':
                k = False
                for a, b in l1:
                    ai = a + i
                    bj = b + j
                    if 0 <= ai <= n - 1 and 0 <= bj <= n - 1 and la[ai][bj] != 0 and l[ai][bj] == 'b':
                        la[i][j] = la[ai][bj]
                        k = True
                        break
                if not k:
                    tb+=1
                    la[i][j] = tb
    print(tr,tb)
#多次操作，每次动四个。
#由bug:a 数组的使用可能导致不同类型的晶矿混淆，不如使用一个简单的 visited 数组来表示是否已访问
#且不能保证处理完全，所以不如dfs将一类类彻底找出（积累次手法，用栈来处理！！！！！！！）
k = int(input())
for _ in range(k):
    n = int(input())
    l = [input() for i in range(n)]
    la = [[0] * n for i in range(n)]
    l1 = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    def dfs(x, y, t):
        s= [(x, y)]
        while s:
            cx, cy = s.pop()
            for dx, dy in l1:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l[nx][ny] == t:
                    visited[nx][ny] = True
                    s.append((nx, ny))
    visited = [[False] * n for _ in range(n)]
    r = 0
    b = 0
    for i in range(n):
        for j in range(n):
            if l[i][j] == 'r' and not visited[i][j]:
                visited[i][j] = True
                r += 1
                dfs(i, j, 'r')
            elif l[i][j] == 'b' and not visited[i][j]:
                visited[i][j] = True
                b += 1
                dfs(i, j, 'b')
    print(r,b)