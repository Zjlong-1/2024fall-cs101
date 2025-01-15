#最后有希望的是每个1都在里面，0都不在。用—1，+1来刻画，则是列表中最大的元素
a,b,k=map(int,input().split())
l=[[0]*b for _ in range(a)]
for _ in range(k):
    r,s,p,t=map(int,input().split())
    for i in range(max(0, r - 1 - (p - 1) // 2), min(r  + (p - 1) // 2, a )):
        for j in range(max(0, s - 1 - (p - 1) // 2), min(b , s  + (p - 1) // 2)):
            if t==0:
                l[i][j]-=1
            else:
                l[i][j]+=1
x=max(max(i) for i in l)
print(sum(i.count(x) for i in l))