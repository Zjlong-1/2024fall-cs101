n=input()
t='hello'
k=0
for i in n:
    if i==t[k]:
        k+=1
    if k==5:
        print('YES')
        break
if k!=5:
    print('NO')

#另：用python中的高级函数
import re
s = input()
r = re.search('h.*e.*l.*l.*o', s)
print(['YES', 'NO'][r==None])

#我思路的源泉：
s = input()
s = s.lower()

dp = [0] * 5
data = 'hello'
cnt = 0

for c in s:
    if c == data[cnt]:
        dp[cnt] += 1
        cnt += 1

    if cnt == 5:
        break

if sum(dp) == 5:
    print('YES')
else:
    print('NO')
