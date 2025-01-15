n=int(input())
l=list(map(int,input().split()))
l.sort()
ans=[]
la=[False]*n
l1=[]
def p(t,l1,la):
    if t==n:

        ans.append(' '.join(map(str, l1[:])))
    for i in range(n):
        if not la[i]:
            l1.append(l[i])
            la[i]=True
            p(t+1,l1,la)
            l1.pop()
            la[i]=False
p(0,l1,la)
ans=sorted(set(ans))
for i in ans:
    print(i)
#有极大的bug,‘13 432 1’字典序小于‘5 2 5 2’
#干脆在一开始就剔除
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = []
la = [False] * n
l1 = []
def p(t, l1, la):
    if t == n:
        ans.append(' '.join(map(str, l1[:])))
    else:
        for i in range(n):
            if i > 0 and l[i] == l[i - 1] and not la[i - 1]:
                continue
            if not la[i]:
                l1.append(l[i])
                la[i] = True
                p(t + 1, l1, la)
                l1.pop()
                la[i] = False
p(0, l1, la)
for i in ans:
    print(i)
