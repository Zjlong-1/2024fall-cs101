n=int(input())
for i in range(n):
    t=0
    s=int(input())
    a=int(input())
    la=list(map(int,input().split()))
    b=int(input())
    lb=list(map(int,input().split()))
    t=0
    for k in la:
        for j in lb:
            if k + j == s:
                t += 1 * lb.count(j)*la.count(k)
                lb = [x for x in lb if x != j]
                la= [x for x in la if x != k]
    print(t)
    #超时了，考虑高级函数（本质思想一样，都是去重）
from collections import Counter
n=int(input())
for i in range(n):
    t=0
    s=int(input())
    a=int(input())
    la=list(map(int,input().split()))
    b=int(input())
    lb=list(map(int,input().split()))
    t=0
    counta=Counter(la)
    countb=Counter(lb)
    set(la)
    set(lb)
    for k in la:
        for j in lb:
            if k + j == s:
                t += 1 * counta[k]*countb[j]
    print(t)
#用for太慢了，每一个都要跑。换为in，可以小一个平方量级
from collections import Counter
n=int(input())
for i in range(n):
    s=int(input())
    a=int(input())
    la=list(map(int,input().split()))
    b=int(input())
    lb=list(map(int,input().split()))
    t=0
    counta=Counter(la)
    countb=Counter(lb)
    la=set(la)
    for k in la:
        if s-k in lb:
            t+=counta[k]*countb[s-k]
    print(t)
