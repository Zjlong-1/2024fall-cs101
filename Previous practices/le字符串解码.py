#好题，要多个记录空间：
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        res,multi='',0
        for i in s:
            if i=='[':
                stack.append((res,multi))
                res, multi = '', 0
            elif i==']':
                res1,multi1=stack.pop()
                res=res1+multi1*res
            elif '0'<=i<='9':
                multi=multi*10+int(i)
            else:
                res+=i
        return res
#还可以递归：
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)

