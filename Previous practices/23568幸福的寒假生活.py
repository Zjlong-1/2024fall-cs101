#数据读错了，是日期
n=int(input())
l=[]
for i in range(n):
    a,b,c=map(float,input().split())
    if a<b:
        l.append((a,b,c))
k=len(l)
la=[0]*(k+1)
l.sort()
for i in range(1,k+1):
    la[i]=int(l[i-1][2])
    for j in range(1,i):
        if l[i-1][0]>l[j-1][1]:
            la[i]=max(la[i],la[j]+int(l[i-1][2]))
print(max(la))
#数据读错了，是日期
n=int(input())
l=[]
for _ in range(n):
    a,b,c=input().split()
    a1,a2=map(int,a.split('.'))
    b1,b2=map(int,b.split('.'))
    if a1==1:
        a=a2-6
    else:
        a=a2+25
    if b1==1:
        b=b2-6
    else:
        b=b2+25
    if b<=45:
        l.append((a,b,int(c)))
k=len(l)
la=[0]*k
l.sort()
la[0]=l[0][-1]
for i in range(1,k):
    la[i]=l[i][-1]
    for j in range(i):
        if l[i][0]>l[j][1]:
            la[i]=max(la[i],la[j]+l[i][2])
print(max(la))