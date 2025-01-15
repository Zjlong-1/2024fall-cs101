class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ans,max1=1,1
        nums=list(set(nums))
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                max1+=1
            else:
                ans=max(ans,max1)
                max1=1
            ans=max(max1,ans)#防止一直连续，使得ans 没有及时更新（或者说，防止最后一个连续数列是最大的，要保证能更新。
        return ans
#还可以用字典（反正要去重），可以省一步sort():但每一个都进行了循环遍历，不见得快多少。
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
