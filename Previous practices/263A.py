n = 0
m = 0
for i in range(5):
    a = list(map(int, input().split()))
    if 1 in a:
        n=i
        m=a.index(1)
print(abs(2-n)+abs(2-m))

