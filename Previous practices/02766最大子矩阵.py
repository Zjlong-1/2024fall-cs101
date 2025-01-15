n = int(input())
nums = []
while len(nums) < n * n:
    nums.extend(input().split())
matrix = [list(map(int, nums[i * n:(i + 1) * n])) for i in range(n)]
ans=-float('inf')
for i in range(n):
    la=[0]*n
    for j in range(i,n):
        for k in range(n):
            la[k]+=matrix[j][k]
        max_ =la[0]
        c=la[0]
        for k in la[1:]:
            c=max(c+k,k)
            max_=max(max_,c)
        ans=max(ans,max_)
print(ans)
