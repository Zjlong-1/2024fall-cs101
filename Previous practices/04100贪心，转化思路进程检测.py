k=int(input())
for i in range(k):
    n=int(input())
    l=[False]*n
    l1=[list(map(int,input().split())) for _ in range(n)]
    t=0
    while False in l[0:n-1]:
        i=0
        a=0
        b=0
        t+=1
        while i<n-1:
            if l[i]:
                i+=1
                continue
            if l[i+1]:
                i+=1
                continue
            if a==b==0:
                a=l1[i][0]
                b=l1[i][1]
                l[i]=True
            if a<=l1[i+1][1]:
                b=l1[i+1][1]
                l[i+1]=True
            elif b>=l1[i][0]:
                a=l1[i][0]
                l[i+1]=True
            i+=1
print(t)
#想复杂了，而且不完备，还会死循环。直接从问题入手即可。
#两区间有交集等价与现将区间按上界排序，只要第一个的上界小于第二个的下界即可。
k=int(input())
for i in range(k):
    n=int(input())
    l1=[list(map(int,input().split())) for _ in range(n)]
    l1.sort(key=lambda x:x[1])
    t=0
    ta=-1
    for j in l1:
        a,b=j[0],j[1]
        if ta<a:
            t+=1
            ta=b#这表示之前的容不下你，所以必须自己开一个，由于你的区间更宽松，所以后面原本可以容纳的也会被这个新开的容纳。所以每次更新后，不需要再管前面的了。
    print(t)