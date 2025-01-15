#因为是随便找一个，不妨从最左和最右开始：
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    left,right=0,n-1
    max1,min1=n,1
    k=True
    while left<right:
        if l[left]==max1:
            max1-=1
            left+=1
        elif l[left]==min1:
            min1+=1
            left+=1
        elif l[right]==max1:
            max1-=1
            right-=1
        elif l[right]==min1:
            min1+=1
            right-=1
        else:
            k=False
            print(left+1,right+1)
            break
    if k:
        print(-1)