class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        start,end=0,0
        n=len(nums)
        s=0
        ans=0
        while start <n:
            while s<k:
                s+=nums[end]
                end += 1
#本来想用滑动窗口来做，但发现元素不一定大于0.所以只能老套的用sum储存，再判断差了：
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import Counter
        n=len(nums)
        l=[0]*(n+1)
        ans=0
        for i in range(1,n+1):
            l[i]=l[i-1]+nums[i-1]
        l1=Counter(l)
        for i in l1:
            ans+=l1[i]*l1[k-i]
#这又踩入陷阱了，以为要I<J，la[j]-la[i]==k:
#所以不能一次就全部统计完，要跟着指针同时进行统计：
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        n=len(nums)
        s=[0]*(n+1)
        for i in range(1,n+1):
            s[i]=s[i-1]+nums[i-1]
        ans=0
        count=defaultdict(int)
        for i in range(n+1):
            ans+=count[s[i]-k]
            count[s[i]]+=1
        return ans
#也可以节省空间，不用S，反正和是在不断加的：
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = s = 0
        cnt = defaultdict(int)
        cnt[0] = 1  # s[0]=0 单独统计
        for x in nums:
            s += x
            ans += cnt[s - k]
            cnt[s] += 1
        return ans
