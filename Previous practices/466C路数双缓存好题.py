n=int(input())
l=list(map(int,input().split()))
la=[0]*n
t1=0
t2=0
la[0]=l[0]
l1=set(l)
for i in range(1,n):
    la[i]+=la[i-1]+l[i]
if l1=={0}:
    print((n-1)*(n-2)//2)
elif la[n-1]%3!=0:
    print(0)
else:
    k=0
    while 3*la[k]!=la[n-1]:
        k+=1
        if k==n:
            break
    if k==n:
        print(0)
    else:
        y=k+1
        while l[y]==0:
            if y==n-1:
                break
            y+=1
            t1+=1
        while 3*la[k]!=2*la[n-1]:
            k+=1
            if k==n:
                break
        if k==n:
            print(0)
        else:
            y = k + 1
            while l[y] == 0:
                if y==n-1:
                    break
                y += 1
                t2 += 1
            print((t2+1)*(t1+1))
#看似很好，但如果有0，-1，1交错就会出错，算法不对。
#判断节点周围0的个数其实也就是sum为节点的个数找出所有点，再相乘，并用双指针去确保不出界。
#再ON**2左右
n=int(input())
l=list(map(int,input().split()))
la=[0]*n
la[0]=l[0]
t=0
for i in range(1,n):
    la[i]+=la[i-1]+l[i]
if la[n-1]%3!=0:
    print(0)
else:
    for i in range(n):
        if la[i]*3==la[n-1]:
            for j in range(i+1,n-1):
                if la[j] * 3 == la[n - 1] * 2:
                    t += 1
    print(t)
#又超时了，计数太笨拙,再次用记忆型缓存
n=int(input())
l=list(map(int,input().split()))
la=[0]*n
la[0]=l[0]
for i in range(1,n):
    la[i]+=la[i-1]+l[i]
if la[n-1]%3!=0:
    print(0)
else:
    a,b=0,0
    for i in range(n):
        if 0<i<n-1 and la[i]*3==la[n-1]*2:
            a+=b
        if la[i]*3==la[n-1]:
            b+=1
    print(a)

