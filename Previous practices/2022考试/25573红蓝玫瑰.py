#两个列表，一个原组，一个反转组
s=input()
n=len(s)
la1=[0]*n
la2=[0]*n
if s[0]=='B':
    la1[0]=1
else:
    la2[0]=1
for i in range(1,n):
    if s[i]=='R':
        la1[i]=min(la1[i-1],la2[i-1]+2)
        la2[i]=min(la1[i-1]+1,la2[i-1]+1)
    else:
        la1[i]=min(la1[i-1]+1,la2[i-1]+1)
        la2[i]=min(la2[i-1],la1[i-1]+2)
print(la1[-1])

