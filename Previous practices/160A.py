n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
t=0
k=0
for i in range(n):
    if t*2>sum(l):
        break
    else :
        t+=l[i]
        k=i+1
print(k)

#另一差不多版，一直加到大于一半

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
b = 0
c = sum(a)
k = 0
for i in a:
    b += i
    k += 1
    if b > c/2:
        break
print(k)