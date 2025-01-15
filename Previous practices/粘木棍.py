n,m=map(int,input().split())
l=list(map(int,input().split()))
#关键在于m不动，递归n
results=[]
def dfs(nums):
    k=len(nums)
    if k==m:
        results.append(max(nums)-min(nums))
        return
    for i in range(k):
        a=nums[i]
        nums2=nums[:]
        nums2.pop(i)
        k2=k-1
        for j in range(k2):
            b=nums[j]
            nums3=nums2[:]
            nums3.pop(j)
            nums3.insert(i,a+b)
            dfs(nums3)
dfs(l)
print(min(results))