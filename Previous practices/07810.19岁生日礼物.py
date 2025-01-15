def solve(t):
    if t%19==0:
        return True
    s=set()
    t=str(t)
    for i in range(len(t)-1):
        s.add(t[i:i+2])
    if '19' in s:
        return True
    else:
        return False
n=int(input())
for _ in range(n):
    if solve(int(input())):
        print('Yes')
    else:
        print('No')