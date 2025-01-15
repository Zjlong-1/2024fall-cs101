a=int(input())
n=0
for i in range(a):
    m=map(int,input().split())
    b=sum(m)
    if b>1:
        n+=1
    else:
        n=n
print(n)



#或者直接用count来数数：
print(sum(input().count('1')>1 for x in range(int(input()))))