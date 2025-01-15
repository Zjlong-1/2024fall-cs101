class Solution:
    def trap(self, height: List[int]) -> int:
        start,s2=0,0
        end=0,0
        ans=0
        p=True
        for i in range(1,len(height)):
            if p and height[s2]>=height[i]:
                s2=i
            elif p and height[s2]<height[i]:
                p=False
                end=i
            elif not p and height[end]<height[i]:
                end=i
            elif not p and height[end]>=height[i]:
                p=True
                start,s2=i,i
#写着写着发现找到起点与终点还不够，还要记录每一段的长度，必须要用栈来处理了。但改一下思路，从纵向来看，这又是可行的了（双指针）
#这个思路十分巧妙，一层一层计算。
class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        stack=[]
        for i in range(len(height)):
            while stack and height[i]>height[stack[-1]]:
                k=stack.pop()
                if not stack:
                    break
                z=stack[-1]
                w=i-z-1
                h=min(height[z],height[i])-height[k]
                ans+=h*w
            stack.append(i)
        return ans
#另外还可以用动态规划：对于下标 i，下雨后水能到达的最大高度等于下标 i 两边的最大高度的最小值，下标 i 处能接的雨水量等于下标 i 处的水能到达的最大高度减去 height[i]。
#朴素的做法是对于数组 height 中的每个元素，分别向左和向右扫描并记录左边和右边的最大高度，然后计算每个下标位置能接的雨水量
#栈是横向考虑，而DP是纵向考虑，两种是不同的角度。
#eftMax[0]=height[0]，rightMax[n−1]=height[n−1]。两个数组的其余元素的计算如下：
#当 1≤i≤n−1 时，leftMax[i]=max(leftMax[i−1],height[i])；
#当 0≤i≤n−2 时，rightMax[i]=max(rightMax[i+1],height[i]
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans
#双指针再次优化：使用 height[left] 和 height[right] 的值更新 leftMax 和 rightMax 的值。如果 height[left]<height[right]，则必有 leftMax<rightMax（因为右边的只可能更大，而要求的是取小）
#还有一个巧妙的点是左右有一个会停留在最高点，因此最后会在最高点相遇，而最高点处无法接雨水，于是可以直接跳过，不学要考虑
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1

        return ans


