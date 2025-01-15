n=input()
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    t=0
    for k in range(a,min(b,len(n))):
        if n[k]==n[k-1]:
            t+=1
    print(t)
    #超时了！！！
n=input()
m=int(input())
l=[0]*len(n)
k=[]
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        l[i]=1
for i in range(m):
    a, b = map(int, input().split())
    k.append(sum(l[a-1:b-1]))
print(*k,sep='\n')
#
a=input()
s=[0]*(len(a))
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        s[i]=s[i-1]+1
    else:
        s[i]=s[i-1]
#print(s)
m=int(input())
for _ in range(m):
    r,l=map(int,input().split())
    print(s[l-1]-s[r-1])

#再改进
n = input()
m = int(input())
l = [0] * (len(n) - 1)
for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        l[i] = 1
prefix_sum = [0] * (len(n))
for i in range(1, len(n)):
    prefix_sum[i] = prefix_sum[i - 1] + l[i - 1]
k = []
for i in range(m):
    a, b = map(int, input().split())
    k.append(prefix_sum[b - 1] - prefix_sum[a - 1])
print(*k, sep='\n')
#提前sum（自然形成），再做减法，可以使时间减少不少


