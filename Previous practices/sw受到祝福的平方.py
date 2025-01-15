from math import sqrt
def square(x):
    return  int(sqrt(x))**2==x!=0
t=input()
n=len(t)
def solve(i):
    for j in range(i,n):
        if square(int(t[i:j+1])):
            if j==n-1:
                return True
            if solve(j+1):
                return True
    return False
if solve(0):
    print('Yes')
else:
    print('No')
#还可以先预处理，计算所有的平方数（放在集合里）。