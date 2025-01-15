n,m=map(int,input().split())
l=list(map(int,input().split()))
def solve(d):
    min1,max1=min(l),max(l)
    if min1>1 or max(l)<m:
        return 1
    
#好题，好难想的思路：
#要去寻找这个“未出现的序列"的最短长度，不妨这样去看待一个问题，以M=3为例，既有3种音符 123。首先这样去想，长度为1的子序列，是不是 1和2和3？长度为2的子序列 是不是[123]和[123]两个集合中任选一个？按照前后顺序排起来？长度为3的子序列，是不是集合[123] 和[123] 和[123]三个集合从前往后，每次取一个，按照前后顺序排起来？
n,m=map(int,input().split())
l=list(map(int,input().split()))
ans=1
s=set()
for i in l:
    s.add(i)
    if len(s)==m:
        ans+=1
        s.clear()
print(ans)