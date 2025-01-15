def solve():
    e, f = map(int, input().split())
    n = int(input())
    l = []
    if e==f:
        print('The minimum amount of money in the piggy-bank is 0.')
        return
    if e>f:
        print('This is impossible.')
        return
    for i in range(n):
        a, b = map(int, input().split())
        l.append((a, b))
    la = [[0] + [-1] * (f - e) for i in range(n)]
    l.sort(key=lambda x: x[1])
    for j in range(0, f - e + 1, l[0][1]):
        la[0][j] = (j // l[0][1]) * l[0][0]
    for i in range(1, n):
        la[i] = la[i - 1][:]
        for j in range(l[i][1], f - e + 1):
            if la[i][j - l[i][1]] != -1 and la[i][j] != -1:
                la[i][j] = min(la[i][j - l[i][1]] + l[i][0], la[i][j])
            elif la[i][j - l[i][1]] != -1:
                la[i][j] = la[i][j]
            elif la[i][j] != -1:
                la[i][j] = la[i][j - l[i][1]] + l[i][0]
    k = la[n - 1][f - e]
    if k != -1:
        print(f'The minimum amount of money in the piggy-bank is {k}.')
    else:
        print('This is impossible.')
t=int(input())
for _ in range(t):
    solve()
#太麻烦了，要优化：
def solve():
    e, f = map(int, input().split())
    n = int(input())
    l = [tuple(map(int, input().split())) for _ in range(n)]
    k = f - e
    dp = [float('inf')] * (k + 1)
    dp[0] = 0
    for value, weight in l:
        for j in range(weight, k + 1):
            if dp[j - weight] != float('inf'):
                dp[j] = min(dp[j], dp[j - weight] + value)

    if dp[k] != float('inf'):
        print(f'The minimum amount of money in the piggy-bank is {dp[k]}.')
    else:
        print('This is impossible.')
t = int(input())
for _ in range(t):
    solve()

