n,m=map(int,input().split())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
#qian i ge zai changduwei k d quyunei

la=[0]*(1+m)
for i in range(n):
    for j in range(m,0,-1):
        t=j-l[i][1]
        if 0<=t<=l[i][0]<j and l[i][0]+l[i][1]<=j:
            k=min(t,l[i][0])
            la[j]=max(la[j],la[k]+1)
        elif 0<=t<=l[i][0]<j:
            la[j] = max(la[j], la[t] + 1)
        elif l[i][0]+l[i][1]<=j:
            la[j] = max(la[j], la[l[i][0]] + 1)
print(la[-1])

#还可以先统一化预处理，包含同一个点的不同区间显然是互斥的，不妨先将所有的都加进去
#最后就转化为了区间合并问题：
# 23n2300011072(X)
def generate_intervals(x, width, m):
    temp = []
    for start in range(max(0, x-width+1), min(m, x+1)):
        end = start+width
        if end <= m:
            temp.append((start, end))
    return temp


n, m = map(int, input().split())
plans = [tuple(map(int, input().split())) for _ in range(n)]
intervals = []
for x, width in plans:
    intervals.extend(generate_intervals(x, width, m))
intervals.sort(key=lambda x: (x[1], x[0]))
cnt = 0
last_end = 0
for start, end in intervals:
    if start >= last_end:
        last_end = end
        cnt += 1
print(cnt)