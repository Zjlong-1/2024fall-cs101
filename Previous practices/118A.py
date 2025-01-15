n=input()
n=n.lower()
l=[]
for k in n:
    if k!='a' and  k!='e' and k!='i'and k!='o'and k!='u' and k!='y':
        l.append('.'+k)
print(''.join(l))