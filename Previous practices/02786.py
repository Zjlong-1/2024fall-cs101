n=int(input())
l=[1,2]
a = 1
b = 2
while True:
    b=2*b+a
    a=(b-a)//2
    t=b%32767
    if t==1 and (2*b+a)%32767==2:
        break
    l.append(t)
for i in range(n):
    m=int(input())
    print(l[m%len(l)-1])
#因为给的数据比较大，所以要用模周期来简化一下,但要注意周期是1,2 同时出现才开始的。
