class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

#通俗的写法：
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            ans=ans^i
        return ans