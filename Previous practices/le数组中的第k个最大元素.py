class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l=Counter(nums)
        l=sorted(l.items())
        t=-1
        while k>0:
            if l[t][1]>=k:
                return l[t][0]
            else:
                k-=l[t][1]
                t-=1
#还有最快的桶排序：from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = (pow(10, 4) * 2 + 1)
        buckets = [0] * n

        base = pow(10, 4)
        for num in nums:
            num = num + base
            buckets[num] = buckets[num] + 1

        for i in reversed(range(n)):
            if buckets[i] == 0:
                continue
            if k <= buckets[i]:
                return i - base
            else:
                k = k - buckets[i]