a,b=map(int,input().split())
t=0
while b>=a:
    b=b-a+1
    t+=a
t+=b
print(t)
#算法超时了，哈哈
a,b=map(int,input().split())
t=0
k=b%(a-1)
if b==0:
    print(0)
elif k==0:
    print(b+b//(a-1)-1)
else:
    print(b+b//(a-1))