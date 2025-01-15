#加保护圈，用以简便运算
n,m,k=map(int,input().split())
ll=[[0]*(m+2) for i in range(n+2)]
t=0
p=[]
for i in range(k):
    x,y=map(int,input().split())
    ll[x][y]=1
    if ll[x][y]==ll[x+1][y+1]==ll[x+1][y]==ll[x][y+1] or ll[x][y]==ll[x][y-1]==ll[x-1][y]==ll[x-1][y-1] or ll[x][y]==ll[x][y-1]==ll[x+1][y]==ll[x+1][y-1] or ll[x][y]==ll[x-1][y+1]==ll[x-1][y]==ll[x][y+1]:
        t=i+1
        p.append(t)
p.append(t)
print(p[0])
