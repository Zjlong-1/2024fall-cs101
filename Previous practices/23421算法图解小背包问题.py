n,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for i in range(n):
    l3.append((l1[i],l2[i]))
l3.sort(key=lambda x:x[1])
la=[[0]*(b+1) for _ in range(n)]
for i in range(n):
    for j in range(l3[i][1],b+1):
        la[i][j]=max(la[i-1][j-l3[i][1]]+l3[i][0],la[i-1][j])
print(la[n-1][b])