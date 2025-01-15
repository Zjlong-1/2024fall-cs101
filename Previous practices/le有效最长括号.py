class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 考虑s[i−dp[i−1]−1],而且不能定义前多少个，因为要用DP定位之前的状态，因此需要知道终点。
        n = len(s)
        la = [0] * n
        if n < 2:
            return 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i >= 2:
                        la[i] = la[i - 2] + 2
                    else:
                        la[i] = 2
                elif i - 1 - la[i - 1] >= 0 and s[i - 1 - la[i - 1]] == "(":
                    if i - 2 - la[i - 1] >= 0:
                        la[i] = la[i - 1] + la[i - 2 - la[i - 1]] + 2
                    else:
                        la[i] = la[i - 1] + 2
        return max(la)
#非常强的栈解法：
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                # 左括号则直接压栈
                stack.append(i)
            else:
                # 右括号则弹栈
                stack.pop()
                if not stack:
                    # 若栈为空，则当前i成为新的不匹配位置
                    stack.append(i)
                else:
                    # 若栈不空，则计算有效长度
                    length = i - stack[-1]
                    max_len = max(max_len, length)

        return max_len