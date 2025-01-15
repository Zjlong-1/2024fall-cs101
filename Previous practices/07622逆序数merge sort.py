n=int(input())
l=list(map(int,input().split()))
def solve(i):
    x=0
    for j in range(i+1,n):
        if l[i]>l[j]:
            x+=1
    return x
ans=0
for i in range(n-1):
    ans+=solve(i)
print(ans)
#超时了，用mergesort优化：(非常巧妙）
ans=0
def merge(l):
    global ans
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        merge(left)
        merge(right)
        le=re=k=0
        while len(left)>le and len(right)>re :
            if left[le]<=right[re]:
                l[k]=left[le]
                le+=1
            else:
                l[k]=right[re]
                re+=1
                ans+=len(left)-le
            k+=1
        while len(left)>le:
            l[k]=left[le]
            le+=1
            k+=1
        while len(right)>re:
            l[k]=right[re]
            re+=1
            k+=1
n=int(input())
l=list(map(int,input().split()))
merge(l)
print(ans)

