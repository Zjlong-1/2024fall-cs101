n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
l1 = [[False] * n for _ in range(n)]
l2 = [ (0, 1), (1, 0)]
l1[0][0] = True
def f(l,s):
    for a,b in l2:
        x, y = s[0]+a, s[1]+b
        if x==y==n-1:
            return True
        if 0<=x<n and 0<=y<n:
            if l[x][y]==0:
                if not l1[x][y]:
                    l1[x][y]=True
                    if f(l,(x,y)):
                        return True
                else:continue
            else:
                continue
    return False
if f(l,(0,0)):
    print('Yes')
else:
    print('No')
#如果要记录路径，可以用栈来储存。

