h,l,n=map(int,input().split())
l1=list(map(int,input().split()))
l1.sort()
k=l1[n//2]
t=l/k
print(f'{h-5*t**2:.2f}')
