a,b=input().split()
for i in range(0,len(b)-len(a)+1):
    if a==b[i:i+len(a)]:
        print(i)
        break

