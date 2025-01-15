n=int(input())
for i in range(1,n):
    if i<=2:
        print('*'*i)
    else:
        print('*'+' '*(i-2)+'*')
print('*'*n)
