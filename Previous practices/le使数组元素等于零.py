class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n=len(nums)
        l=[0]*n
        l[0]=nums[0]
        ans=0
        for i in range(1,n):
            l[i]=l[i-1]+nums[i]
        for i in range(n):
            if nums[i]==0 :
                if l[i]*2==l[-1]:
                    ans+=2
                if abs(l[i]*2-l[-1])==1:
                    ans+=1
        return ans
#还可以省空间，而且判断可以用True，0时是False