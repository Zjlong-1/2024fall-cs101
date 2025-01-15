n=input()
m=len(n)
t=0
for i in range(m-6):
    if n[i]==n[i+1]==n[i+2]==n[i+3]==n[i+4]==n[i+5]==n[i+6]:
        t+=1
if t>0:
    print('YES')
else :
    print('NO')
#条件判断
s=input()
print(['NO','YES']['0'*7 in s or '1'*7 in s])
#还可以用all()（判断型函数）