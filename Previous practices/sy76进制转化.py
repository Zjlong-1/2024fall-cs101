n,m=map(int,input().split())
l=[(10,'A'),(11,'B'),(12,'C'),(13,'D'),(14,'E'),(15,'F')]
k=[]
for i in range(10, 0,-1):
    if m ** i <= n < m ** (i + 1):
        k.append(n // (m ** i))
        n = n % (m ** i)
    else:k.append(0)
k.append(n)
k1=[]
while len(k)>1 and k[0]==0:
    k=k[1:]
for i in k:
    if i>=10:
        i=l[i-10][1]
        k1.append(i)
    else:
        k1.append(i)
print(*k1,sep='')

