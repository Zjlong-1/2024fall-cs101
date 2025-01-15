n=int(input())
l=[]
for i in range(n):
    k=input()
    a=k.count('++')
    b=k.count('--')*(-1)
    l.append(a)
    l.append(b)
print(sum(l))
#另：
n=int(input())
x=0
for i in range(n):
    k=input()
    if '++'in k:
        x+=1
    else:
        x-=1
print(x)

