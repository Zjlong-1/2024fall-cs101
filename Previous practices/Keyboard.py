x='qwertyuiopasdfghjkl;zxcvbnm,./'
n=input()
m=input()
l=[]
if n=='R':
    for i in m:
        y=x.index(i)
        l.append(x[y-1])
else:
    for i in m:
        y = x.index(i)
        l.append(x[y + 1])
print(''.join(l))