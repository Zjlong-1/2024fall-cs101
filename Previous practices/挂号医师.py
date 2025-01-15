n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append((a,i+1))
l.sort(key=lambda x:(x[0],x[1]))
print(l[0][1])
