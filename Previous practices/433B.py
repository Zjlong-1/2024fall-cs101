n=int(input())
k=list(map(int,input().split()))
m=int(input())
k1=sorted(k)
for i in range(m):
    a,b,c=map(int,input().split())
    if a==1:
        print(sum(k[b-1:c]))
    else:
        print(sum(k1[b - 1:c]))
#又是同样的超时，考虑经典手法：在数据读取的同时加上得到片段和，最后只需做一次减法即可。
n=int(input())
k=list(map(int,input().split()))
m=int(input())
k2=sorted(k)
t=[0]*(n+1)
t1=[0]*(n+1)
for o in range(1,n+1):
    t[o]=t[o-1]+k[o-1]#这里采用递加的方法，比sum快很多
    t1[o]=t1[o-1]+k2[o-1]
for i in range(m):
    a,b,c=map(int,input().split())
    if a==1:
        print(t[c]-t[b-1])
    else:
        print(t1[c]-t1[b-1])