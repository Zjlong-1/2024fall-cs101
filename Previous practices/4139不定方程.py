a,b,c=map(int,input().split())
t=0
for x in range(c//a+1):
    if (c-a*x)%b==0 and c-a*x>=0:
        t+=1
print(t)