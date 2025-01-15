#两边无先后顺序，只要确定数量即可,只要最早确定不是，x的倍数即可
t=int(input())
for i in range(t):
    n, x = map(int, input().split())
    l=list(map(int,input().split()))
    k=sum(l)
    la=[]
    if k%x!=0:
        print(n)
    else:
        for j in range(n):
            if l[j]%x!=0:
                la.append(j)
        if len(la)==0:
            print(-1)
        else:
            print(max(n-la[0]-1,la[-1]))











