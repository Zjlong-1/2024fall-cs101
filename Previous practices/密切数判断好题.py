#不需要判断素数的素因数分解法，不可能是合数（因为已经被之前的除完了，或者说没有比他更小的素数了）
def p(t):
    s=set()
    while t%2==0:
        t=t//2
        s.add(2)
    for i in range(3,int(t**0.5)+1):
        while t%i==0:
            t=t//i
            s.add(i)
    if t>2:
        s.add(t)
    return s
a,b=map(int,input().split(','))
if p(a)==p(b):
    print("YES")
else:
    print('NO')