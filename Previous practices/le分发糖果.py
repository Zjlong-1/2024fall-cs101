class Solution:
    def candy(self, ratings: List[int]) -> int:
        la = [0] * len(ratings)
        from collections import deque
        q1 = deque()
        q1.append(ratings[0])
        for i in range(1, len(ratings)):
            x = q1.pop()
            if x > ratings[i]:
                q1.append(x)
                q1.append(ratings[i])
            else:
                la[i - 1] = 1
                t = 1
                while q1:
                    t += 1
                    la[i - t] = t
                    q1.pop()
                q1.append(ratings[i])
        t = -1
        while q1:
            la[t] = -t
            q1.pop()
            t -= 1
        ratings = list(reversed(ratings))
        lb= [0] * len(ratings)
        q2 = deque()
        q2.append(ratings[0])
        for i in range(1, len(ratings)):
            x = q2.pop()
            if x > ratings[i]:
                q2.append(x)
                q2.append(ratings[i])
            else:
                la[i - 1] = max(1,la[i - 1])
                t = 1
                while q2:
                    t += 1
                    la[i - t] = max(la[i-t],t)
                    q2.pop()
                q2.append(ratings[i])
        t = -1
        while q2:
            la[t] =max(-t,la[t])
            q2.pop()
            t -= 1
        return sum(la)
#是最大值，而不是sum!!!!!!!(左右规则弄错了）,这是写过的最长代码了！
class Solution:
    def candy(self, ratings: List[int]) -> int:
        la = [0] * len(ratings)
        from collections import deque
        q1 = deque()
        q1.append(ratings[0])
        for i in range(1, len(ratings)):
            x = q1.pop()
            if x > ratings[i]:
                q1.append(x)
                q1.append(ratings[i])
            else:
                la[i - 1] = 1
                t = 1
                while q1:
                    t += 1
                    la[i - t] = t
                    q1.pop()
                q1.append(ratings[i])
        t = -1
        while q1:
            la[t] = -t
            q1.pop()
            t -= 1
        ratings = list(reversed(ratings))
        lb = [0] * len(ratings)
        q2 = deque()
        q2.append(ratings[0])
        for i in range(1, len(ratings)):
            x = q2.pop()
            if x > ratings[i]:
                q2.append(x)
                q2.append(ratings[i])
            else:
                lb[i - 1] = 1
                t = 1
                while q2:
                    t += 1
                    lb[i - t] = t
                    q2.pop()
                q2.append(ratings[i])
        t = -1
        while q2:
            lb[t] = -t
            q2.pop()
            t -= 1
        lb = list(reversed(lb))
        for i in range(len(ratings)):
            la[i] = max(la[i], lb[i])
        return sum(la)
#事实上已经太复杂了，可以不用队列，递增时，大则加T+1，否则1：
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [0] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1

        right = ret = 0
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            ret += max(left[i], right)

        return ret
