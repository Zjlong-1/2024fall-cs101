from functools import lru_cache
@lru_cache(maxsize=None)
def solve3(n):
    if n==1:
        return 1
    else:
        return 2*solve3(n-1)+1

@lru_cache(maxsize=None)
def solve4(n):
    min1=float('inf')
    if n==1:
        return 1
    for i in range(n):
        min1=min(min1,2*solve4(i)+solve3(n-i))
    return min1
for i in range(1,13):
    print(solve4(i))


