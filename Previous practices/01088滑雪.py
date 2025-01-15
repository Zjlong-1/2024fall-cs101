r,c=map(int,input().split())
l=[]
l2=[]
for i in range(r):
    l1=list(map(int,input().split()))
    for j in range(c):
        l.append((l1[j],i,j))
    l2.append(l1)
l.sort()
la=[[1]*c for _ in range(r)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for a,b,d in l:
    for dx, dy in directions:
        b1, d1 = b+ dx, d+ dy
        if 0 <= b1 < r and 0 <=d1 < c and l2[b1][d1] < a:
            la[b][d] = max(la[b][d], la[b1][d1] + 1)
print(max(la[i][j] for i in range(r) for j in range(c)))
