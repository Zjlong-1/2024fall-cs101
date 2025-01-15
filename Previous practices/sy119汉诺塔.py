l=[]
def h(a,b,c,n):
    if n==1:
        l.append(f'{a}->{c}')
        return
    h(a,c,b,n-1)
    l.append(f'{a}->{c}')
    h(b,a,c,n-1)
n=int(input())
h('A','B','C',n)
print(len(l))
for i in l:
    print(i)