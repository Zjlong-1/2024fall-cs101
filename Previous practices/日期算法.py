a,b,c=map(int,input().split('-'))
n=int(input())
q=[1,3,5,7,8,10,12]
p=[4,6,9,11]
for i in range(n):
    if b in q:
        if c==31:
            c=1
            if b==12:
                b=1
                a+=1
            else:
                b+=1
        else:
            c+=1
    elif b in p:
        if c==30:
            c=1
            b+=1
        else:
            c+=1
    elif b==2:
        if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
            if c==29:
                c=1
                b+=1
            else:
                c+=1
        else:
            if c==28:
                c=1
                b+=1
            else:
                c+=1
if b<10:
    b='0'+str(b)
if c<10:
    c='0'+str(c)
print(a,b,c,sep='-')



