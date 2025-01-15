import math
n=int(input())
l=[]
for i in range(6,int(math.sqrt(n))+1):
    if n%i==0:
        l.append(i)
if l==[]:
    for i in range(1,6):
        if n % i == 0 and int(n/i)>=6:
            l.append(i)
    print(max(l))
else:
    print(n //min(l))
#另一思路：a+b+c>=6
#故直接从6开始不断加，除非数很离谱。一般不会超时
n=int(input())
i = 1 + 2 + 3
while n%i != 0:
    i += 1
else:
    print(n // i)


