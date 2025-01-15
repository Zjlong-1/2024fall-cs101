t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    if n<m :
        print('NO')
    elif n==m:
        print('YES')
    elif n%3!=0:
        print('NO')
    else:
        while n!=m*3 and n*2!=m*3:
            if n%3!=0:
                break
            else:
                n=n//3
        if n!=m*3 and n*2!=m*3:
            print('NO')
        else:
            print('YES')
#少了一些情况，用递归更好，同时不用担心超时，算就完了。
from functools import lru_cache
@lru_cache(maxsize=None)
def a(n, m):
    if n == m:
        return True
    if n < m or n % 3 != 0:
        return False
    if a((n // 3) * 2, m):
        return True
    if a(n // 3, m):
        return True
    return False
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if a(n, m):
        print('YES')
    else:
        print('NO')