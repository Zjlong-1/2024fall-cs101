n=int(input())
l=[100,20,10,5,1]
a=0
for i in l:
    a+=int(n/i)
    n=n%i
print(a)
