t,m=map(int,input().split())
l=[]
k=0
for _ in range(m):
    a,b=map(int,input().split())
    l.append((b/a,a,b))
l.sort()
for i in l:
    if i[1]<=t:
        t-=i[1]
        k+=i[2]
print(k)
#错误，想的太简单了。要递归。
#正解：
#非常不纯的动态规划，极易让人误解（没必要为了哪一点空间来变得难理解）
t,m=map(int,input().split())
l=[[0]*t for _ in range(m)]
k=[]
for i in range(m):
    k.append([int(j) for j in input().split()])
la=[0]*(t+1)
for i in range(m):
    for j in range(t,k[i][0]-1,-1):
        la[j]=max(la[j],la[j-k[i][0]]+k[i][1])#la[j]事实上是之前i-1时的储藏，不断更新。
print(la[-1])
#t,m=map(int,input().split())
l=[[0]*t for _ in range(m)]
k=[]
for i in range(m):
    k.append([int(j) for j in input().split()])
la=[0]*(t+1)
for i in range(m):
    for j in range(k[i][0],t+1):
        la[j]=max(la[j],la[j-k[i][0]]+k[i][1])
print(la[-1])#这是不行的，因为每次都会更新，这会导致前面一部分未被调用就更新（导致加上了j时的情况，更新出现BUG）（因为要用调用la[j]事实上是之前i-1时的储藏，不断更新。），从而发生错误。