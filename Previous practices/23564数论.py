from collections import defaultdict
def solve():
    n = int(input())
    cnt = defaultdict(int)
    ans = 0
    if n==1:
        return 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ans += 1
            while n % i == 0:
                n = n // i
                cnt[i] += 1
                if cnt[i]==2:
                    return 0
    if n>1:
        ans+=1
    if ans % 2 == 0:
        return 1
    else:
        return -1
print(solve())
