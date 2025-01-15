n=int(input())
l=list(map(int,input().split()))
m=int(input())
p=list(map(int,input().split()))
p.sort()
l.sort()
a=0
for i in range(n):
    for j in range(m):
        if abs(l[i]-p[j])<=1:
            p[j]=10000
            a+=1
            break
print(a)
