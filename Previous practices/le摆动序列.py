class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        k=nums[0]
        ans=1
        h=1
        while nums[h]==k:
            h+=1
            if h==len(nums):
                return 1
        if nums[0]>nums[h]:
            t=True
            ans+=1
        else:
            t = False
            ans+=1
        k=nums[h]
        for i in range(h+1,len(nums)):
            if t:
                if nums[i]>k:
                    ans+=1
                    t=False
            else:
                if nums[i]<k:
                    ans+=1
                    t=True
            k=nums[i]
        return ans
#贪心即可，每次取最有利于下一项的数。但要注意把前面全相等的情况用while循环弄掉。
#我的方法的另一简化写法：
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        prevdiff = nums[1] - nums[0]
        ret = (2 if prevdiff != 0 else 1)
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                ret += 1
                prevdiff = diff

        return ret

#或用DP定义down 和up 两种数组。
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        up = [1] + [0] * (n - 1)
        down = [1] + [0] * (n - 1)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = max(up[i - 1], down[i - 1] + 1)
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = max(up[i - 1] + 1, down[i - 1])
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return max(up[n - 1], down[n - 1])
#还可以优化空间：
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        up = down = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1

        return max(up, down)


