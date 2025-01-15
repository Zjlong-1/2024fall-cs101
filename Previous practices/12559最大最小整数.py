n=int(input())
l=input().split()
l1=[]
for i in range(n):
    l1.append((int(l[i])/(10**len(l[i])-1),i))
l1.sort()
l2=sorted(l1,reverse=True)
a=''.join(l[i] for _ , i in l1)
b=''.join(l[i] for _,i in l2)
print(b+' '+a)
#字符串可以比大小（直接就是字典序），即量化一种性质，（每两个数之间的排序方式固定），以此为大小并以此进行排序。由于没有内置函数可以对自己定义的‘大小’进行sort（函数映射转化为唯一），所以要自己写sort的代码，考虑其中较简单的冒泡排序。
# O(n^2)
n = int(input())
nums = input().split()
for i in range(n - 1):
    for j in range(i+1, n):
        #print(i,j)
        if nums[i] + nums[j] < nums[j] + nums[i]:
            nums[i], nums[j] = nums[j], nums[i]

ans = "".join(nums)
nums.reverse()
print(ans + " " + "".join(nums))

