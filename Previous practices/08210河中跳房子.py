#这里可以证明整体最优确实要求局部最优，每次都只要考虑最小区间的断点即可
#但是这一遇到了一个问题，也就是有多个最短区间怎么办
l,n,m=map(int,input().split())
lens=[int(input()) for _ in range(n)]
d=[lens[0]]
mind=d[0]
idx=0#第0个开头
for i in range(1,n):
    k=lens[i]-lens[i-1]
    d.append(k)
    if k<
#有多个最短区间怎么办，这个问题解决不了，不妨枚举每一个距离，看是否能够实现，并进行二分查找
l, n, m = map(int, input().split())
lens = [0] + [int(input()) for _ in range(n)] + [l]


def can(d):
    idx = 0
    cnt = 0
    for i in range(1, n + 2):
        if lens[i] - lens[idx] >= d:
            idx = i
        else:
            cnt += 1
    if cnt <= m:
        return True
    return False


left = 0
right = l
while left < right:
    t = (left + right) // 2 + 1
    if can(t):
        left = t
    else:
        right = t - 1
print(left)


