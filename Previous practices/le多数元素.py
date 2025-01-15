class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=Counter(nums)
        a=l.most_common(1)
        return a[0][0]
#还可以取巧：
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]