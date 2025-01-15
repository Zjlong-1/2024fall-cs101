n=int(input())
for i in range(n):
    t=input()
    if len(t)>10:
        print(t[0]+str(len(t)-2)+t[-1])
    else:
        print(t)
