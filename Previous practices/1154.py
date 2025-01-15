n=input().split()
a=0
for i in n:
    a+=int(i)
b=int(a/3)
m=0
l=[]
for i in n:
    if int(i)!=b:
        m=b-int(i)
        l.append(m)
print(*l)

#直接排序（确定变量）
a = list(map(int, input().split()))
a.sort()
print(a[3]-a[0],a[3]-a[1],a[3]-a[2])
