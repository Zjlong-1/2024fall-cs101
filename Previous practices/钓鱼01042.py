while True:
    n=int(input())
    if n==0:
        break
    t=int(input())*60
    f=list(map(int,input().split()))
    di=list(map(int,input().split()))
    ti=list(map(int,input().split()))
    l=[]
    for i in range(n):
        ans = [0] * n
        ans1 = 0
        k=f[0:i+1]
        t1=t
        t1-=sum(ti[0:i])*5
        while t1>=5 and max(k)>0:
            j=k.index(max(k))
            t1-=5
            ans1+=k[j]
            ans[j]+=5
            k[j]=max(0,k[j]-di[j])
        ans[0]+=t1
        l.append((ans1,ans))
    l.sort(key=lambda x:(x[0],x[1]) ,reverse=True)#这里细节决定成败！！！！！
    print(*l[0][1],sep=', ')
    print(f'Number of fish expected: {l[0][0]}')
    print()






