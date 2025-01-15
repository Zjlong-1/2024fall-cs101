n=int(input())
while n!=1:
    if n%2==1:
        a=n
        n=n*3+1
        print("{}*3+1={}".format(a,n))
    else:
        a=n
        n=n//2
        print("{}/2={}".format(a,n))