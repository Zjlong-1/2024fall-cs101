n,t=map(int,input().split())
l=list(map(int,input().split()))
s=sum(l)
def solve():
    if s<t:
        return 0
    la = [True] + [False] * s
    la[l[0]] = True
    for i in range(1, n):
        for j in range(s, l[i] - 1, -1):
            if la[j - l[i]]:
                la[j] = True
    for i in range(t,s+1):
        if la[i]:
            return i
print(solve())


