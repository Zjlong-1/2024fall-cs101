class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        for [i,j] in queries:
            for k in range(i,j+1):
                if nums[k]>0:
                    nums[k]-=1
        if nums==[0]*len(nums):
            return True
        else:
            return False
#毫无疑问超时了，原因在于一个一个减时间实在是太长了，考虑到减的都是1，不妨每次都减去，看最后是不是都是非正。
#区间都减去相同的数，差分是首选，不要忘记了这个强大的工具。
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]):
        n=len(nums)
        l=[0]*(n+1)
        sum=0
        for [i,j] in queries:#事实上i，j 就可以了。
            l[i]+=1
            l[j+1]-=1
        for i in range(n):
            sum+=l[i]
            if sum<nums[i]:
                return False
        return True
#用zip压缩函数可以更快：
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            # 区间 [l,r] 中的数都加一
            diff[l] += 1
            diff[r + 1] -= 1

        for x, sum_d in zip(nums, accumulate(diff)):
            # 此时 sum_d 表示 x=nums[i] 要减掉多少
            if x > sum_d:  # x 无法变成 0
                return False
        return True