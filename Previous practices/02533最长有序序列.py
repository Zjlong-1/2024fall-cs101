n=int(input())
l=list(map(int,input().split()))
end=[1]*n
for i in range(1,n):
    for j in range(i):
        if l[i]>l[j]:
            end[i]=max(end[j]+1,end[i])
print(max(end))
#确定结束点，简单DP。