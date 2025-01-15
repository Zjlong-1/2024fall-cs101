n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
la1=[0]*n
la2=[0]*n
la1[0]=l1[0]
la2[0]=l2[0]
max1=0
max2=0
for i in range(n):
        la1[i]=max(la1[i],max2+l1[i])
        la2[i]=max(la2[i],max1+l2[i])
        max1=max(max1,la1[i])
        max2=max(max2,la2[i])
print(max(max(la1),max(la2)))
#超时了，最大值要记录。
#之前的代码：
n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
la1=[0]*n
la2=[0]*n
la1[0]=l1[0]
la2[0]=l2[0]
for i in range(n):
    for j in range(i):
        la1[i]=max(la1[i],la2[j]+l1[i])
        la2[i]=max(la2[i],la1[j]+l2[i])
print(max(max(la1),max(la2)))
