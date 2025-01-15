n=int(input())
x=bin(n)[2:]
def solve(x):
    k=len(x)
    for i in range(k//2):
        if x[i]!=x[k-1-i]:
            print('No')
            return
    print('Yes')
    return
solve(x)
