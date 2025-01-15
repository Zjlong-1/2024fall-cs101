n=int(input())
m=input().split()
t=0
k=0
for i in range(n):
    t=t+int(m[i])
    if t<0:
        k+=1
        t=t+1
print(k)





