n=int(input())
l=[]
la=[1]*n
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
l.sort()
for i in range(n):
    for j in range(i):
        if l[j][1]<=l[i][0]:
            la[i]=max(la[i],la[j]+1)
print(max(la))
#简单DP ，以头排序，使得可以接的都是前面的。