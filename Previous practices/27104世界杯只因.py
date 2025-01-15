n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(n):
    l1.append((i+1-l[i],i+1+l[i]))
l1.sort()
def solve():
    i = 0
    ans = 0
    end = 1
    start = 1
    while i < n:
        if l1[i][0] <= start:
            end = max(l1[i][1], end)
            if end>=n:
                return ans+1
            i += 1
        else:
            ans += 1
            start = end
print(solve())

