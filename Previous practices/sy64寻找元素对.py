n=int(input())
l=list(map(int,input().split()))
k=int(input())
m=0
for i in range(n-1):
    for j in range(i+1,n):
        if l[i]+l[j]==k:
            m+=1
print(m)
