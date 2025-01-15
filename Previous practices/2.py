n=int(input())
m=input().split()
l=''
a=[]
for i in m:
    if len(i)+len(l)>80:
        l.rstrip()
        a.append(l)
        l=i+' '
    else:
        l+=i+' '
else:
    a.append(l.rstrip())
print('\n'.join(a))