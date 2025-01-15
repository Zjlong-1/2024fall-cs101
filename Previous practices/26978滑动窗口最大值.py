from collections import deque
n,k=map(int,input().split())
l=list(map(int,input().split()))
q=deque()
q.append(0)
ans=[]
for i in range(1,k):
    while q and l[q[-1]]<=l[i]:
        q.pop()
    q.append(i)
ans.append(l[q[0]])
for i in range(k,n):
    while q and l[q[-1]]<=l[i]:
        q.pop()
    q.append(i)
    while q[0]<=i-k:
        q.popleft()
    ans.append(l[q[0]])
print(*ans)
