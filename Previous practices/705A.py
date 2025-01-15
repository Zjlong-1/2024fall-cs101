n=int(input())
l=[0]*(n*3)
for i in range(n*3):
    if (i+1)%3==0:
        l[i]='that'
    elif (i+1)%3==1:
        l[i]='I'
    elif (i+1)%6==5:
        l[i]='love'
    else:
        l[i]='hate'
l[-1]='it'
print(*l)
