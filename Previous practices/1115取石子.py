from functools import lru_cache
lru_cache(maxsize=None)
def solve(a,b):
    a,b=min(a,b),max(a,b)
    if b%a==0:
        return True
    k=b//a
    for i in range(1,k+1):
        if  not solve(a,b-a*i):
            return True
    return False
while True:
    a,b=map(int,input().split())
    if a==b==0:
        break
    if solve(a,b):
        print('win')
    else:
        print('lose')



#[a/b]≥2, 则先手有选择权，可以切换到必胜的情况，设a=t*b+r,0<=r<b,(r,b)只有胜与不胜两种可能，
#如果(r,b)胜，则先手转化为（b+r,b）就可以必胜，如果（r,b）败，转化为（r,b）就可以必胜
#至于[a/b]<=1时就递归
def solve(a,b):
    a,b=min(a,b),max(a,b)
    if b%a==0:
        return True
    k=b//a
    if k>=2:
        return True
    else:
        return not solve(a,b-a)
while True:
    a,b=map(int,input().split())
    if a==b==0:
        break
    if solve(a,b):
        print('win')
    else:
        print('lose')
