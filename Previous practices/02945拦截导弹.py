n=int(input())
l=list(map(int,input().split()))
la=[-1]*n
for i in range(n-1,-1,-1):
    m=1
    for j in range(n-1,i,-1):
        if l[i]>=l[j] and la[j]+1>m:
            m=la[j]+1
    la[i]=m
print(max(la))
#la指的是以第I个位置为起点的最长非增数列长度。
