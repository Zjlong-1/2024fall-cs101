n=int(input())
l=list(map(int,input().split()))
t=0
m=0
o=0
for i in l:
    if i%2==0:
        t+=1
        if t>1:
            m=1
for y in l:
    if (y-m)%2==0:
        o=l.index(y)+1
print(o)

#另:整体思想+二项选择（弄出简单情况，其余用else)

n = int(input())
a = list(map(int, input().split()))
a = [i % 2 for i in a]
sum_val = sum(a)
if sum_val == 1:
    print(a.index(1) + 1)
else:
    print(a.index(0) + 1)




#新颖的字符串思路：
n = int(input())
l = input().split()
m = ''
for i in range(n):
    m = m + str(int(l[i])%2)

if m.count('1')==1:
    print(int(m.index('1'))+1)
else:
    print(int(m.index('0'))+1)

#最快的头脑风暴
useless = input()
a = [int(x)%2 for x in input().split()]
print(a.index(sum(a)==1)+1)




