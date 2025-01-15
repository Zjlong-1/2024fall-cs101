class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        la=[0]*len(nums)
        la[0]=nums[0]
        for i in range(1,len(nums)):
            la[i]=max(nums[i],la[i-1]+nums[i])
        return max(la)
#dp:la表示以第i个结尾的最大子数组
#还可以再优化：（实时记录，省去最后的求max）
class Solution:
    def maxSubArray(self, nums):
        pre = 0
        maxAns = nums[0]
        for x in nums:
            pre = max(pre + x, x)
            maxAns = max(maxAns, pre)
        return maxAns
#还可以分而治之（mergesort的核心思想）：对于 [l,r] 的 rSum，同理，它要么等于「右子区间」的 rSum，要么等于「右子区间」的 iSum 加上「左子区间」的 rSum，二者取大。
#当计算好上面的三个量之后，就很好计算 [l,r] 的 mSum 了。我们可以考虑 [l,r] 的 mSum 对应的区间是否跨越 m——它可能不跨越 m，也就是说 [l,r] 的 mSum 可能是「左子区间」的 mSum 和 「右子区间」的 mSum 中的一个；它也可能跨越 m，可能是「左子区间」的 rSum 和 「右子区间」的 lSum 求和。三者取大。
class Solution:
    class Status:
        def __init__(self, lSum, rSum, mSum, iSum):
            self.lSum = lSum  # 左段和
            self.rSum = rSum  # 右段和
            self.mSum = mSum  # 最大和
            self.iSum = iSum  # 区间和

    def pushUp(self, l, r):
        # 合并两个子区间的状态
        iSum = l.iSum + r.iSum
        lSum = max(l.lSum, l.iSum + r.lSum)
        rSum = max(r.rSum, r.iSum + l.rSum)
        mSum = max(max(l.mSum, r.mSum), l.rSum + r.lSum)
        return self.Status(lSum, rSum, mSum, iSum)

    def get(self, a, l, r):
        # 递归分治处理
        if l == r:
            return self.Status(a[l], a[l], a[l], a[l])
        m = (l + r) // 2
        lSub = self.get(a, l, m)
        rSub = self.get(a, m + 1, r)
        return self.pushUp(lSub, rSub)

    def maxSubArray(self, nums):
        # 求解最大子数组和
        return self.get(nums, 0, len(nums) - 1).mSum
#还可以贪心：从左到右一个一个加，如果sum小于0，则重新找子串
class Solution:
    def maxSubArray(self, nums):
        # 类似寻找最大最小值的题目，初始值一定要定义成理论上的最小最大值
        result = float('-inf')  # Python中可以用 float('-inf') 来表示最小值
        sum = 0

        for num in nums:
            sum += num
            result = max(result, sum)
            # 如果 sum < 0，重新开始找子序串
            if sum < 0:
                sum = 0

        return result
