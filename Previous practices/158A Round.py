n,k=map(int,input().split())
a=list(map(int,input().split()))
m=0
for b in range(n):
    if a[b-1]>=a[k-1] and a[b-1]>0:
        m+=1
    else:
        m=m
print(m)
