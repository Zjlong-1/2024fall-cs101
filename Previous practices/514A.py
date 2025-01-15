n=input()
l=[]
for i in range(len(n)):
    if int(n[i])>=5:
        l.append(9-int(n[i]))
    else:
        l.append(int(n[i]))
if n[0]=='9':
    l[0]=9
print(*l,sep='')