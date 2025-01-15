from collections import deque
n,k=map(int,input().split())
l=list(map(int,input().split()))
q=deque()
ans=[]
for i in range(n):
     while q and l[q[-1]]<=l[i]:
         q.pop()
     q.append(i)
     if q[0]+k-1<i:
         q.popleft()
     if q[-1]>=k-1:
         ans.append(l[q[0]])
print(*ans)
#duque加双指针，好题