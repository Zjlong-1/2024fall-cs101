n=input()
l=[]
t=1
if len(n)==1:
    l.append(1)
for i in range(len(n)-1):
    if n[i]!=n[i+1]:
        t+=1
    if n[i]==n[i+1]:
        l.append(t)
        t=1
    l.append(t)
print(max(l))