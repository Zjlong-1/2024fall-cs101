#这个题的难点在于什么时候走，走多远。解题的切入点十分巧妙：在不得不走时，才判断怎么走，这就与跳跃游戏1形成了完美的过渡
#难怪叫贪心：思想就一句话：每次在上次能跳到的范围（end）内选择一个能跳的最远的位置（也就是能跳到max_far位置的点）作为下次的起跳点 ！
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        end,k=0,0
        far=0
        ans=0
        for i in range(n-1):
            far=max(far,i+nums[i])
            if i==end:
                end=far
                ans+=1
        return ans
#还可以DP，但时间复杂度太高了。

