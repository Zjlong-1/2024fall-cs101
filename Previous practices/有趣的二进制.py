n=int(input())
a=input().split()
b=input().split()
t=0
for i in range(n):
    for j in range(i,n):
        if a[i]==b[j]:
            b[i:j+1]=[b[j]]+b[i:j]
            t+=j-i
            break
if a==b:
    print(t)
else:
    print(-1)

