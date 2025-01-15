n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b,i))
l.sort()
la=[[l[0][2]]]
min1=l[0][1]
lb=[l[0][1]]
for i in range(n):
    if l[i][0]>min1:
        k=lb.index(min1)
        lb[k]=l[i][1]
        min1=min(lb)
        la[k].append(l[i][2])
    else:
        lb.append(l[i][1])
        la.append([l[i][2]])
        min1 = min(lb)
for i in range(len(la)):
    la[i].sort()
la.sort()
s={}
for i in range(len(la)):
    for j in la[i]:
        s[j]=i
print(len(la)-1)
for i in range(n):
    print(s[i])
#果然超时了，算法太复杂了。最大最小可以用堆来减少时间
import heapq
n=int(input())
l=[]
m=1
number=[0]*n
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b,i))
l.sort()
t=[]
heapq.heappush(t,[l[0][1],1])
number[l[0][2]]=1
for i in range(1,n):
    min1=heapq.heappop(t)
    if min1[0]<l[i][0]:
        heapq.heappush(t,[l[i][1],min1[1]])
        number[l[i][2]] = min1[1]
    else:
        m+=1
        heapq.heappush(t,min1)
        heapq.heappush(t, [l[i][1],m])
        number[l[i][2]]=m
print(len(t))
for _ in number:
    print(_)