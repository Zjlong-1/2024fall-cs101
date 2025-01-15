n,m=map(int,input().split())
l=[]
for _ in range(n):
    l.append(int(input()))
la=[[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        la[i][j]=min(la[i][j-1]+l[j-1],max(la[i-1][j-1],l[j-1]))
print(la[-1][-1])
#转2维矩阵：
n, m = map(int, input().split())
l = [int(input()) for _ in range(n)]

# 用滚动数组代替二维数组
prev = [float('inf')] * (n + 1)
curr = [0] * (n + 1)

for i in range(1, m + 1):
    for j in range(1, n + 1):
        curr[j] = min(curr[j - 1] + l[j - 1], max(prev[j - 1], l[j - 1]))
    prev, curr = curr, [float('inf')] * (n + 1)

print(prev[-1])
#但解法有问题，看我用两个数组完善：.小丑了，这个题目无法用DP，关键卡在i-1,j时最大在哪个组不确定，导致无法接上
#考虑brute force,暴力解决.二分查找确定最小最大数（定义函数判断）
n,m=map(int,input().split())
l=[]
sum2=0
maxl=0
for _ in range(n):
    k=int(input())
    sum2+=k
    l.append(k)
    maxl=max(maxl,k)
def can(x):
    sum1=0
    cnt=1
    for i in l:
        if sum1+i>x:
            cnt+=1
            sum1=i
            if cnt>m:
                return False
        else:
            sum1+=i
    return True
start,end=maxl,sum2
while start<end:
    t=(start+end)//2
    if can(t):
        end=t
    else:
        start=t+1
print(end)
#自己写在循环了的sum和max慢，可以直接用内置。
