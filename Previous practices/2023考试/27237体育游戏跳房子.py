from collections import deque
while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    def bfs():
        q=deque()
        inq=set()
        q.append((n,''))
        inq.add(n)
        while q:
            k,l=q.popleft()
            if k==m:
                return l
            if 3*k not in inq:
                q.append((3*k,l+'H'))
                inq.add(3*k)
            if k//2 not in inq:
                q.append((k//2,l+'O'))
                inq.add(k//2)
    ans=bfs()
    print(len(ans))
    print(ans)