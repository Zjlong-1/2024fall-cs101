#因为只有三种数，所以可以一个一个排，指针一样，不断向前走：
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        start=0
        for i in range(n):
            if nums[i]==0:
                nums[i],nums[start]=nums[start],nums[i]
                start+=1
        for j in range(start,n):
            if nums[j]==1:
                nums[j], nums[start] = nums[start], nums[j]
                start += 1
#除了单指针，还可以双指针：
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
