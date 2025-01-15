h=int(input())*2
n=int(input())
l=[]
t=0
h-=n*0.5
for i in range(n):
    a,b=map(float,input().split())
    l.append((a*b,a,b))
l.sort(key=lambda x:-x[0])
for i in l:
    if h==0:
        break
    elif h>=5/i[1]:
        h-=5/i[1]
        t+=5*i[2]
    else:
        t+=h*i[1]*i[2]
        h=0
print(f'{t:.1f}')
#知道性价比就好做了


