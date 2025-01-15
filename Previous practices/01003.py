while True:
    n = float(input())
    if n==0.00:
        break
    else:
        p=0
        while n>0:
            n=n-1/(p+2)
            p+=1
    print(str(p)+' '+'card(s)')