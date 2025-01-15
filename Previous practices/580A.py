n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n-1):
    if l[i+1]>=l[i]:
        a.append(0)
    else:
        a.append(1)
k=1
u=1
for i in a:
    if i==0:
        k+=1
        u=max(k,u)
    else:
        k=1
print(u)
#先将比大小转化为数相同元素个数，之后在用max来不断更新值
#另外一个很巧的方法：
n = int(input())
a = [int(i) for i in input().split()]

f = [0] * n
f[0] = 1
max_value = 1
for i in range(1, len(a)):
    if a[i] >= a[i - 1]:
        f[i] = f[i - 1] + 1
        if f[i] > max_value:
            max_value = f[i]
    else:
        f[i] = 1

print(max_value)


