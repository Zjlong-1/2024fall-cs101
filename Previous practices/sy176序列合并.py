n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=[]
while len(l1)>0 and len(l2)>0:
    if l1[0]>=l2[0]:
        l.append(l2[0])
        l2=l2[1:]
    else:
        l.append(l1[0])
        l1=l1[1:]
if  len(l1)>0:
    l+=l1
else:
    l+=l2
print(*l)
#超时在于切片，可以不切，每次加一即可
n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=[]
i,j=0,0
while i<n and j<m:
    if l1[i]>=l2[j]:
        l.append(l2[j])
        j+=1
    else:
        l.append(l1[i])
        i+=1
while i<n:
    l.append(l1[i])
    i+=1
while j<m:
    l.append(l2[j])
    j+=1
print(*l)
#竟然超时了，换普通方法。
n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=l1+l2
print(*sorted(l))

