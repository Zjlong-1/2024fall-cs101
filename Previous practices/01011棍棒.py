import math
def find_factors(n):
    factors = set()
    for i in range(1,int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(factors)
while True:
    n=int(input())
    if n==0:
        break
    l=list(map(int,input().split()))
    s=sum(l)
    def solve(d):  # d表示大小
        k = s // d
        la = [0] * k
        def dfs(idx):
            if idx == n:
                return True
            for j in range(k):
                if la[j] + l[idx] <= d:
                    la[j] += l[idx]
                    if dfs(idx + 1):
                        return True
                    la[j] -= l[idx]
                if la[j]==0:
                    break
            return False
        return dfs(0)
    factors=find_factors(s)
    max1=max(l)
    for i in factors:
           if i>=max1 and solve(i):
               print(i)
               break
#dfs改了很多次还是超时，只能换算法了。
#事实上，只要换一个角度就可以了，先不把木棍弄出来，而是一个一个地把棍子接满，这样可以节省许多时间。
#还有最后一个的超强剪枝：
while True:
    n=int(input())
    if n==0:
        break
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    s=sum(l)
    use=[False]*64
    def solve(k,left,d):
        if k == left == 0:
            return True
        if left == 0:
            left = d
        for i in range(n):
            if not use[i] and l[i]<=left:
                if i>0 and l[i]==l[i-1] and not use[i-1]:
                    continue
                use[i]=True
                if solve(k-1,left-l[i],d):
                    return True
                use[i]=False
                if l[i]==left or left==d:
                    break
        return False
    def ans():
        for i in range(l[0],s//2+1):
            if s%i==0 and solve(n,0,i):
                return i
        return s
    print(ans())
