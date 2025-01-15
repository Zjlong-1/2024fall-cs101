n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    x=b-a+1
    l=[1]*(x+1)
    for i in range(3,x+1):
        l[i]=l[i-1]+l[i-2]
    print(l[x])