def solve():
    n=int(input())
    l=list(map(int,input().split()))
    la = [0] * n
    la[0] = max(0, l[0])
    if n==1:
        return la[0]
    la[1]=max(la[0],l[1])
    for i in range(2,n):
        la[i]=max(l[i],l[i]+la[i-2],la[i-1])
    return la[-1]
print(solve())
