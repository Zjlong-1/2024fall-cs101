

n,m=map(int,input().split())
l=[]
a=0
for i in range(m):
    j,k=map(int,input().split())
    l.append((j,k))
l.sort()
for o in range(m-1):
    if l[o][1]>=l[o+1][0]:
        l[o+1]=(l[o][0],max(l[o+1][1],l[o][1]))
        l[o]=(0,0)
while (0,0) in l:
    l.remove((0, 0))
for u in range(len(l)):
    a=a+l[u][1]+1-l[u][0]
print(n-a+1)
print(l)

#这个代码我想了很久也修改了很久，将题目中的问题抽象化。但事实上依题来做会更快：
L, m = map(int, input().split())

dp = [1]*(L+1)

for i in range(m):
    s, e = map(int, input().split())
    for j in range(s, e+1):
        dp[j] = 0

print(dp.count(1))