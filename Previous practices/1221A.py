n=int(input())
for i in range(n):
    k=int(input())
    l=list(map(int,input().split()))
    la={1:0,2:0,4:0,8:0,16:0,32:0,64:0,128:0,256:0,512:0,1024:0,2048:0}
    for j in l:
        if j<=2048:
            la[j]+=1
    for p in la:
        if p==2048:
            break
        la[2*p]+=la[p]//2
    if la[2048]>0:
        print('YES')
    else:
        print('NO')




