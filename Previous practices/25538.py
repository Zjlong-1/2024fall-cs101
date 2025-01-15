n=int(input())
n=bin(n)[2:]
m=n[::-1]
if m==n:
    print('Yes')
else:
    print('No')