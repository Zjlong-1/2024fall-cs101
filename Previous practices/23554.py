n=int(input())
l=list(map(int,input().split()))
k=[]
a=[]
h=[]
for i in range(1,n+1):
    if i in l:
        k.append(i)
    else:
        h.append(i)
for j in l:
    if j not in k:
        a.append(j)
a.sort()
print(*h)
print(*a)


