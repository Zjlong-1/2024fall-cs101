class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        #看错题了，只要求求出右侧看到的人数
        stack=[-1]
        n=len(heights)
        la=[1]*n
        la[-1]=0
        for i in range(n-2,-1,-1):
            while stack and  heights[stack[-1]]<heights[i]:
                stack.pop()
                if stack:
                    la[i]+=1
            if stack and heights[stack[-1]]==heights[i]:
                continue
            stack.append(i)
        return la
