n=int(input())
for i in range(n):
    t=int(input())
    m=0
    for o in range(25):
        if 2**o<=t<2**(o+1):
            m=o
    print(2+t*(t+1)//2-2**(m+2))

