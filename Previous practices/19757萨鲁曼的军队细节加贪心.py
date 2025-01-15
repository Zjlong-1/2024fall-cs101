while True:
    r,n=map(int,input().split())
    if r==n==-1:
        break
    l=list(map(int,input().split()))
    l.sort()
    k=0
    t=0
    a=0
    while k<n-1:
        end=False
        if l[n - 1] <= l[t] + r:
            a+=1
            break
        elif l[k]<=l[t]+r and l[k+1]>l[t]+r:
            a+=1
            h=k
            while l[h]<=l[k]+r:
                if h==n-1:
                    end=True
                    break
                else:
                    h+=1
            t=h
            k=h
            if not end and h==n-1:
                a+=1
        elif l[k+1]<=l[t]+r:
            k+=1
    print(a)
#变量太多，太麻烦了
while True:
    r,n=map(int,input().split())
    if r==-1 and n==-1:
        break
    l=list(map(int,input().split()))
    l.sort()
    i=0
    a=0
    while i<n:
        k=l[i]
        a+=1
        while i<n and l[i]<=k+r :#注意这里不能l[i]<=k+r and i<n 因为计算机是一步一步来的先判断左边再判断右边，所以要先写前置的必要条件。
            i+=1
        k=l[i-1]
        while i<n and l[i]<=k+r:
            i+=1
    print(a)

