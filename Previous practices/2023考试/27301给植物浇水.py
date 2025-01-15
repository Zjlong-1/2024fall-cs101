n,a,b=map(int,input().split())
l=list(map(int,input().split()))
i = 0
a1, b1 = a, b
cnt = 0
while i < n // 2:
    if a1 >= l[i]:
        a1 -= l[i]
    else:
        a1 = a - l[i]
        cnt += 1
    if b1 >= l[n - 1 - i]:
        b1 -= l[n - 1 - i]
    else:
        b1 = b - l[n - 1 - i]
        cnt += 1
    i += 1
if n%2==0:
    print(cnt)
else:
    if a1>=b1:
        if  a1>=l[i]:
            a1-=l[i]
        else:
            a1=a-l[i]
            cnt+=1
    else:
        if b1>=l[n-1-i]:
            b1-=l[n-1-i]
        else:
            b1=b-l[n-1-i]
            cnt+=1
    print(cnt)


