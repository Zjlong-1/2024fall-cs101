n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
if sorted(l)==sorted(l,key=lambda x: x[1]):
    print('Poor Alex')
else:
    print('Happy Alex')
#验证是否顺序即可