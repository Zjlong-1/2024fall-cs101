#看错题了，这是解写出最大连续和：
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s=0
        for i in range(k):
            s+=nums[i]
        ans=s
        t=k-1
        for j in range(k,len(nums)):
            s=s-nums[j-k]+nums[j]
            if s>ans:
                ans=s
                t=j
        return nums[t-k+1:t+1]
#正解：
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q=deque()
        la=[]
        for i in range(k):
            while q and nums[q[-1]]<=nums[i]:
                q.pop()
            q.append(i)
        la.append(nums[q[0]])
        for i in range(k,len(nums)):
            while q and nums[q[-1]]<=nums[i]:
                q.pop()
            q.append(i)
            while q[0]<=i-k:
                q.popleft()
            la.append(nums[q[0]])
        return la
#也可以用堆来做：（即不需要主动维护单调性，堆自动完成了这些事情）
    class Solution:
        def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            n = len(nums)
            # 注意 Python 默认的优先队列是小根堆
            q = [(-nums[i], i) for i in range(k)]
            heapq.heapify(q)

            ans = [-q[0][0]]
            for i in range(k, n):
                heapq.heappush(q, (-nums[i], i))
                while q[0][1] <= i - k:
                    heapq.heappop(q)
                ans.append(-q[0][0])

            return ans
