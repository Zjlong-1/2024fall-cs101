n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
k=0
g=0
for i in l:
    if i<=0:
        k+=1
if k>=m:
    print(-sum(l[0:m]))
else:
    for h in l:
        if h<=0:
            g=h+g
    print(-g)

#事实上列表中位数大于m的都不需要考虑。so，直接限制Range即可（可以避免多分类）
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(m):
    if a[i] > 0:
        break
    ans += a[i]
print(-ans)