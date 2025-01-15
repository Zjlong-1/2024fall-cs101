n,k=map(int,input().split())
l=list(map(int,input().split()))
t=0
p=0
while p<n+1:
    found=False
    for i in range(p,n - 1):
        for j in range(i + 1, n):
            if l[i] + l[j] == k:
                t += 1
                n = j-1
                p=i+1
                found = True
                print(t,i,j)# 设置标志变量为 True
                break  # 跳出内层循环
            if found:  # 如果标志变量为 True，跳出外层循环
                break
    if not found:
        break
print(t)
#算法多余，找到后就可以break
#但复杂过度有许多问题,这真的无力回天了！
#考虑双指针，有简单又快
n,k=map(int,input().split())
l=list(map(int,input().split()))
i,j=0,n-1
t=0
while i<j:
    if l[i]+l[j]==k:
        t+=1
        i+=1
        j-=1
    elif l[i]+l[j]<k:
        i+=1
    else:
        j-=1
print(t)


