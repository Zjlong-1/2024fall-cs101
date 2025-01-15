n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
l1=[l[0][i]*1000+l[-1][i]*10 for i in range(m)]
l2=[l[j][0]+l[j][-1]*100 for j in range(n)]
k=[]
for i in range(n):
    for j in range(m):
        k.append(l[i][j]*(l2[i]+l1[j]))
print(max(k))