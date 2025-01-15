class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        l=[]
        s=set()
        def pai(step):
            if step==n:
                ans.append(l[:])#浅拷贝，非常重要
            for i in nums:
                if i not in s:
                    s.add(i)
                    l.append(i)
                    pai(step+1)
                    s.remove(i)
                    l.pop()
        pai(0)
        return ans