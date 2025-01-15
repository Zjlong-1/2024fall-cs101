class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left,right=0,n-1
        ans=min(height[-1],height[0])*(n-1)
        while left<right:
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            ans=max(ans,min(height[left],height[right])*(right-left))
        return ans
#一个提前终止的小优化：
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height)-1
        max_h = max(height)
        for i in height:
            width = right - left
            if width * max_h < area:
                break
            l_h = height[left]
            r_h = height[right]
            real_height = min(l_h,r_h)
            _area = width*real_height
            if _area>area:
                area=_area
            if l_h < r_h:
                left += 1
            else:
                right -= 1

        return area