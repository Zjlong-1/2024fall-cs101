import sys
sys.setrecursionlimit(800000)
input=sys.stdin.read
data=input().split()
k=int(data[0])
id=1
for _ in range(k):
    m,n=map(int,data[id:id+2])
    id+=2
    l=[]
    for i in range(m):
        l.append(list(map(int,data[id:id+n])))
        id+=n
    i1, j1 = map(int, data[id:id + 2])
    id += 2
    p=int(data[id])
    id+=1
    wh=[[0]*n for i in range(m)]
    l1=[(-1,0),(1,0),(0,1),(0,-1)]
    def solve(x,y):
        for dx,dy in l1:
            nx,ny=dx+x,dy+y
            if 0<=nx<m and 0<=ny<n and l[nx][ny]<wh[x][y] and wh[nx][ny]<wh[x][y]:
                wh[nx][ny]=wh[x][y]
                solve(nx,ny)
    for i in range(p):
        x,y=map(int,data[id:id+2])
        id+=2
        x-=1
        y-=1
        if wh[x][y]<l[x][y]:
            wh[x][y]=l[x][y]
            solve(x,y)
    if wh[i1-1][j1-1]!=0:
        print('Yes')
    else:
        print('No')