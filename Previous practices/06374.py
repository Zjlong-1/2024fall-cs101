n=int(input())
m=input().split()
l=''
a=[]
for i in m:
    if len(i)+len(l)>80:
        l.rstrip()
        a.append(l+'\n')
        l=i+''
    else:
        l+=i+' '
print(*a)#这是错误的！因为用*a来print会导致开头自动产生空格（本身的性质）
#故作以下改进:
n=int(input())
m=input().split()
l=''
a=[]
for i in m:
    if len(i)+len(l)>80:
        l.rstrip()
        a.append(l)
        l=i+''
    else:
        l+=i+' '
else:
    a.append(l.rstrip())
print('\n'.join(a))


