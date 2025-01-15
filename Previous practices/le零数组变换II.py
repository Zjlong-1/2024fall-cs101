class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def solve(nums,l):
            for x,y in zip(nums,accumulate(l)):
                if x>y:
                    return False
            return True
        n=len(nums)
        l=[0]*(n+1)
        k=0
        for i,j,t in queries:
            if solve(nums,l):
                return k
            k+=1
            l[i]+=t
            l[j+1]-=t
        if solve(nums,l):
                return k
        return -1
#果然不是照搬I就可以，在最后2个数据时超时了，太难受了。要优化。
#不一个一个试，采用二分法来解决：
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n=len(nums)
        def check(k):
            l=[0]*(n+1)
            for i,j,t in queries[:k]:
                l[i]+=t
                l[j+1]-=t
            for x,y in zip(nums,accumulate(l)):
                if x>y:
                    return False
            return True
        m=len(queries)
        left,right=0,m+1
        while left<right:
            k=(left+right)//2
            if check(k):
                right=k
            else:
                left=k+1
        return right if right<=m else -1
#自己都感觉还是有很多多余的计算，考虑实时判断更新：（非常牛的算法思想）
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        diff = [0] * (len(nums) + 1)
        sum_d = k = 0
        for i, (x, d) in enumerate(zip(nums, diff)):
            sum_d += d
            while k < len(queries) and sum_d < x:  # 需要添加询问，把 x 减小
                l, r, val = queries[k]
                diff[l] += val
                diff[r + 1] -= val
                if l <= i <= r:  # x 在更新范围中
                    sum_d += val
                k += 1
            if sum_d < x:  # 无法更新
                return -1
        return k