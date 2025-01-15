from math import sqrt
n=int(input())
for i in range(n):
    a,b,c=map(float,input().split())
    if b==0:
        b=-b
    if (b**2-4*a*c)>0:
        x1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
        x2= (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
        print(f"x1={x1:.5f};x2={x2:.5f}")
    elif (b**2-4*a*c)==0:
        x1=-b/(2*a)
        print(f"x1=x2={x1:.5f}")
    else:
        x11=-b/(2*a)
        x12=(sqrt(-b * b + 4 * a * c)) / (2 * a)
        print(f"x1={x11:.5f}+{x12:.5f}i;x2={x11:.5f}-{x12:.5f}i")






