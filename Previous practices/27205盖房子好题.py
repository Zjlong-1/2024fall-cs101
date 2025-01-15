#先考虑每一行（以该行为底的情况）
#卡在处理相等的情况下,细想没必要特殊处理，因为从左到右不断减，处理到最后就没有相同的了（可能先去除的有误差（较小），但最后的是对的，而且只可能更大，即覆盖了错误数据，从而整体正确）
from collections import deque
m,n=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(m)]
ans=[]
for i in range(m):
    h = [0] * n
    for j in range(n):
        if l[i][j]==0:
            k=i
            while k>=0 and l[k][j]==0:
                h[j]+=1
                k-=1
    q=deque()
    for j in range(n):
        while q and h[q[-1]]>h[j]:
            if len(q)==1:
                ans.append(h[q[-1]]*j)
            else:
                ans.append(h[q[-1]]*(j-q[-2]-1))
            q.pop()
        q.append(j)
    while q:
        height = h[q.pop()]
        width = n if not q else n - q[-1] - 1
        ans.append(width*height)
print(max(ans))

