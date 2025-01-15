s=input()
n=len(s)
k,n1=0,n
while n1>=2:
    n1=n1//2
    k+=1
l=[]
for i in range(k//2):
    l.append(s[2**i-1])
    l.append(s[2**(k-i)-1])
if k%2==1:
    l.append(s[2**(k//2)-1])
    l.append(s[2**(k-k//2)-1])
    print(''.join(l))
else:
    l.append(s[2**(k//2)-1])
    print(''.join(l))
