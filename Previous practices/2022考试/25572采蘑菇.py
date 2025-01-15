from collections import deque
n=int(input())
l=[]
cnt=0
l2=[(0,0),(0,0)]
for i in range(n):
    l1=list(map(int,input().split()))
    l.append(l1)
    if cnt!=2:
        for j in range(n):
            if l1[j]==5:
                l2[cnt]=(i,j)
                cnt+=1
x1,y1,x2,y2=l2[0][0],l2[0][1],l2[1][0],l2[1][1]
d=[(0,1),(0,-1),(-1,0),(1,0)]
q=deque()
inq=set()
def solve(x1,y1,x2,y2):
    q.append((x1,y1,x2,y2))
    inq.add((x1,y1,x2,y2))
    while q:
        x3,y3,x4,y4=q.popleft()
        if l[x3][y3]==9 or l[x4][y4]==9:
            return True
        for dx,dy in d:
            nx1,ny1,nx2,ny2=x3+dx,y3+dy,x4+dx,y4+dy
            if 0<=nx1<n and 0<=nx2<n and 0<=ny1<n and 0<=ny2<n and l[nx1][ny1]!=1 and l[nx2][ny2]!=1 and (nx1,ny1,nx2,ny2) not in inq:
                q.append((nx1,ny1,nx2,ny2))
                inq.add((nx1,ny1,nx2,ny2))
    return False
if solve(x1,y1,x2,y2):
    print('yes')
else:
    print('no')
#超内存了，考虑只存一个的位置，而且是在原矩阵的基础上更改（反正相对位置不变）
#好吧，其实不是这个问题，是忘记加检查条件了（in inq)

