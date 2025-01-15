n=int(input())
l=list(map(int,input().split()))
la=[]
for i in range(n):
    la.append((l[i],i+1))
la.sort(key=lambda x :(x[0],x[1]))
print(' '.join(str(la[i][1]) for i in range(n)))
k=sum(la[i][0]*(n-1-i) for i in range(n))
print(f'{k/n:.2f}')
