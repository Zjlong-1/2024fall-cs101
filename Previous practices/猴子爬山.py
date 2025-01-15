m=int(input())
l=[1,3,5]
la=[0]*(1+m)
la[0]=la[1]=1
for i in range(2,m+1):
    for j in l:
        if i-j>=0:
            la[i] += la[i - j]
print(la[-1]%(10**6))

