#看错题了，是线段，不是步数。所以bfsz之后不是最后的答案，还用全部储存并取最小
from collections import deque
board=1
while True:
    w,h=map(int,input().split())
    if w==h==0:
        break
    l=[[' ']*(w+2) for _ in range(h+2)]
    for i in range(1,h+1):
        k=input()
        for j in range(len(k)):
            l[i][j+1]=k[j]
    print(f'Board #{board}:')
    board+=1
    l1=[(0,1,1),(0,-1,2),(1,0,3),(-1,0,4)]
    def bfs(x1,x2,y1,y2):
        ans=[]
        inq=set()
        q=deque()
        q.append((0,y1,x1,-1))
        while q:
            step,y,x,direction1=q.popleft()
            for dx,dy,direction2 in l1:
                nx,ny=dx+x,dy+y
                if 0<=ny<h+2 and 0<=nx<w+2 and (ny,nx,direction2) not in inq :
                    step1 = step
                    if direction1!=direction2:
                        step1=step+1
                    if nx==x2 and ny==y2:
                        ans.append(step1)
                        continue
                    if l[ny][nx]!='X':
                        inq.add((ny, nx,direction2))
                        q.append((step1, ny, nx, direction2))
        if len(ans)==0:
            return 0
        else:
            return min(ans)
    pair=1
    while True:
        x1,y1,x2,y2=map(int,input().split())
        if x1==x2==y1==y2==0:
            break
        k=bfs(x1,x2,y1,y2)
        if k:
            print(f'Pair {pair}: {k} segments.')
        else:
            print(f'Pair {pair}: impossible.')
        pair+=1
    print()