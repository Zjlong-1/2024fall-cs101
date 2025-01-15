n=int(input())
l=list(map(int,input().split()))
for i in l:
    t = 0
    if i==1:
       print('NO')
    elif int(i**0.5)**2==i:
        a=int(i**0.5)
        for k in range(2,int(a**0.5)+1):
            if a%k==0:
                t=2
        if t==2:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')

t=0
l=[]
for a in range(2,10**6):
    for k in range(2, int(a ** 0.5) + 1):
        if a % k == 0:
            t = 2
    if t==0:
        l.append(a**2)
n=int(input())
p=list(map(int,input().split()))
for i in p:
    if i in l:
        print('YES')
    else:
        print('NO')
#又超时了








#终于成功了！！！！用筛法确定素数，同时将素数附上特殊的值，由于有索引就会快，直接判断索引的值是否等于即可（比盲目地用 in快很多）
l=[0]*1000001
l[0]=l[1]=1
for i in  range(2,1001):
    if l[i]==0:
        for k in range(i*i,1000001,i):
            l[k]=1
n=int(input())
p=list(map(int,input().split()))
for i in p:
    if  int(i**0.5)**2==i:
        a=int(i**0.5)
        if l[a]==0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
