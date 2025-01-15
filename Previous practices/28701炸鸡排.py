n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
import sys
sys.setrecursionlimit(200000)
def solve(cnt,k):
    s=sum(l[cnt:])
    m=l[cnt]
    if k==1:
        return (f'{s:.3f}')
    if k==n:
        return (f'{min(l[cnt:]):.3f}')
    if m*k>s:
        return solve(cnt+1,k-1)
    else:
        return (f'{s/k:.3f}')
print(solve(0,k))