class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from bisect import bisect_right
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                k = bisect_right(nums[i:], nums[i - 1]) + i
                if k == n:
                    nums[k - 1], nums[i - 1] = nums[i - 1], nums[k - 1]
                else:
                    nums[k], nums[i - 1] = nums[i - 1], nums[k]
                break
        if i == 1:
            if nums[i] < nums[i - 1]:
                for j in range(n // 2):
                    nums[j], nums[n - j - 1] = nums[n - 1 - j], nums[j]
            else:
                t = (n - i) // 2
                for j in range(t):
                    nums[i + j], nums[n - j - 1] = nums[n - 1 - j], nums[i + j]
        else:
            t = (n - i) // 2
            for j in range(t):
                nums[i + j], nums[n - j - 1] = nums[n - 1 - j], nums[i + j]
#x写了好久，发现还是又问题，bisect要用于递增序列，反正考试不需要省空间，为了一点空间换脑袋想晕，真的没必要。
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from bisect import bisect_right
        n = len(nums)
        t=False
        if n==1:
            return
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                k = bisect_right(nums[i:], nums[i - 1]) + i
                if k == n:
                    nums[k - 1], nums[i - 1] = nums[i - 1], nums[k - 1]
                else:
                    nums[k], nums[i - 1] = nums[i - 1], nums[k]
                t=True
                break
        if i == 1:
            if not t:
                for j in range(n // 2):
                    nums[j], nums[n - j - 1] = nums[n - 1 - j], nums[j]
            else:
                t = (n - i) // 2
                for j in range(t):
                    nums[i + j], nums[n - j - 1] = nums[n - 1 - j], nums[i + j]
        else:
            t = (n - i) // 2
            for j in range(t):
                nums[i + j], nums[n - j - 1] = nums[n - 1 - j], nums[i + j]
#真是老6，还可以相等，卡在最后10个数据了，：
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from bisect import bisect_right
        n = len(nums)
        t=False
        a=False
        if n==1:
            return
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                for k in range(i,n):
                    if nums[i-1]>nums[k]:
                        a=True
                        break
                if a:
                    nums[k - 1], nums[i - 1] = nums[i - 1], nums[k - 1]
                else:
                    if nums[i-1]<nums[-1]:
                        nums[i-1],nums[-1]=nums[-1],nums[i-1]
                    else:
                        nums[i-1],nums[i]=nums[i],nums[i-1]
                t=True
                break
        if i == 1:
            if not t:
                for j in range(n // 2):
                    nums[j], nums[n - j - 1] = nums[n - 1 - j], nums[j]
            else:
                t = (n - i) // 2
                for j in range(t):
                    nums[i + j], nums[n - j - 1] = nums[n - 1 - j], nums[i + j]
        else:
            t = (n - i) // 2
            for j in range(t):
                nums[i + j], nums[n - j - 1] = nums[n - 1 - j], nums[i + j]
#没有意义，写一个缓存组的函数，还是要一点空间比较好：（while循环！！！！！！）
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        firstIndex = -1
        n = len(nums)
        def reverse(nums, i, j):
            while i < j:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                firstIndex = i
                break
        #print(firstIndex)
        if firstIndex == -1:
            reverse(nums, 0, n-1)
            return
        secondIndex = -1
        for i in range(n-1, firstIndex, -1):
            if nums[i] > nums[firstIndex]:
                secondIndex = i
                break
        nums[firstIndex],nums[secondIndex] = nums[secondIndex], nums[firstIndex]
        reverse(nums, firstIndex+1, n-1)
