from functools import lru_cache
lru_cache(maxsize=None)
def solve(n):
    if n==1:
        return 1
    return sum(solve(i) for i in range(1,n))+1
n=int(input())
print(solve(n))
