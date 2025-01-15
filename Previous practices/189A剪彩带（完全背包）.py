l=list(map(int,input().split()))
l1=l[1:]
l1.sort()
n=l[0]
la=[0]*(n+1)
lb=[False]*(n+1)
lb[0]=True
for i in range(l1[0],n+1):
    for j in l1:
        if i>=j:
            if lb[i-j]:
                la[i]=max(la[i-j]+1,la[i])
                lb[i]=True
print(la[n])
#无限次取使得不需要刻意维护。DP即可。