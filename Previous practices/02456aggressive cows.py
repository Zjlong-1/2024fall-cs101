n,c=map(int,input().split())
l=[int(input()) for i in range(n)]
l.sort()
dmax=(l[-1]-l[0])//(c-1)
dmin=1
def d(d1):
    z=l[0]
    k=c-1
    for i in range(1,n):
        if l[i]>=z+d1:
            z=l[i]
            k-=1
        if k==0:
            return True
    return False
ans=0
while dmin<=dmax:
    m=(dmax+dmin)//2
    if d(m):
        dmin=m+1
        ans=m
    else:
        dmax=m-1
print(ans)
#固定公差，判断此公差是否可行，并用二分查找为跨度，简化时间。




