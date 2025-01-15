n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
k=[l[0]*2,(m-l[-1])*2]
for i in range(n-1):
    k.append(l[i+1]-l[i])
print(f"{max(k)/2:.9f}")