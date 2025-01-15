class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        if n<3:
            return []
        nums.sort()
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            k=-nums[i]
            while left<right:
                if nums[left]+nums[right]==k:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                elif nums[left]+nums[right]>k:
                    right-=1
                else:
                    left+=1
        return ans
#去重要保证每加一次都不与之前的数相同。（只要保证前两个指针就可以），事实上，是要在去等是判断，而去等时只有前面两个指针可能动
#小优化：
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:  # 跳过重复数字
                continue
            if x + nums[i + 1] + nums[i + 2] > 0:  # 优化一
                break
            if x + nums[-2] + nums[-1] < 0:  # 优化二
                continue
            j = i+1
            k = n-1
            while j<k:
                s = x + nums[j]+nums[k]
                if s > 0:
                    k-=1
                elif s < 0:
                    j+=1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:  # 跳过重复数字
                        j += 1
#还可以分正负：
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret, hashtable = [], {}
        positive, negative = [], []
        for n in nums:
            if -n in hashtable:
                hashtable[-n] += 1  # 重复值计数
            else:
                hashtable[-n] = 1  # 加入哈希表，并分为正负集合
                if n > 0:
                    positive.append(n)
                else:
                    negative.append(n)

        if 0 in hashtable and hashtable[0] >= 3:
            ret.append([0, 0, 0])

        negative.sort()
        for x in positive:
            if hashtable[-x] > 1 and x * 2 in hashtable:
                ret.append([x, x, -x * 2])
            if x / 2 in hashtable and hashtable[x // 2] > 1:
                ret.append([x, -x // 2, -x // 2])
            for y in negative[
                bisect_right(negative, -x * 2) : bisect_left(negative, -x / 2)
            ]:
                s = x + y
                if s in hashtable:
                    ret.append([x, y, -s])
        return ret