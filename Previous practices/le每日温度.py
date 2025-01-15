class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n=len(temperatures)
        ans = [0] *n
        for i in range(n):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                k=stack.pop()
                ans[k]=i-k
            stack.append(i)
        return ans
#还可以从右往左开始：记录最大候选（省空间，stack最多一个元素）
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n - 1, -1, -1):
            t = temperatures[i]
            while st and t >= temperatures[st[-1]]:
                st.pop()
            if st:
                ans[i] = st[-1] - i
            st.append(i)
        return ans
