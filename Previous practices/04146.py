n=int(input())
a=0
for t in range(1,n+1):
    for x in range(1,n+1):
        for k in range(1,n+1):
            if (t+x)%2==0 and (x+k)%3==0 and (t+x+k)%5==0:
                a=max(a,t+x+k)
print(a)
        