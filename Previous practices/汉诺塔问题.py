def ans(n,a,b,c):
    if n>=2:
        k=list(ans(n-1,a,c,b)+['{}:{}->{}'.format(n,a,c)]+ans(n-1,b,a,c))
    else:
        k=['1:{}->{}'.format(a,c)]
    return k
l=input().split()
n=int(l[0])
a,b,c=l[1],l[2],l[3]
print(*ans(n,a,b,c),sep='\n')
