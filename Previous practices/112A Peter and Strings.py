a=input().lower()
b=input().lower()
n=0
for i in range(len(a)):
    if ord(a[i])>ord(b[i]):
        print(1)
        break
    elif ord(a[i])<ord(b[i]):
        print(-1)
        break
    else :n+=1
if n==len(a):
    print(0)


