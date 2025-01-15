n=int(input())
a,b=1,2
for i in range(n-2):
    a,b=b,a+b
if n==1:
    print(a)
else:
    print(b)