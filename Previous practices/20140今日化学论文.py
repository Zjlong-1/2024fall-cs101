l=input()
stack=[]
res,multi='',0
k=0
if l[k]=='[':
    k+=1
    stack.append(('',1))
for i in l[k:]:
    if i=='[':
        stack.append((res,multi))
        res,multi='',0
    elif i==']':
        res1,multi1=stack.pop()
        res=res1+multi*res
        multi=multi1
    elif '0' <= i <= '9':
        multi = multi * 10 + int(i)
    else:
        res += i
print(res)