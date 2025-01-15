n=int(input())
s=[set() for _ in range(4)]
for i in range(4):
    k=input()
    for j in range(6):
        s[i].add(k[j])
for _ in range(n):
    s1=input()
    t=len(s1)
    visit=[False]*4
    def solve(x):
        if x==t:
            return True
        for i in range(4):
            if not visit[i] and s1[x] in s[i]:
                visit[i]=True
                if solve(x+1):
                    return True
                visit[i]=False
        return False
    def p():
        for i in range(4):
            if s1[0] in s[i]:
                visit[i]=True
                if solve(1):
                    return True
                visit[i]=False
        return False
    if p():
        print('YES')
    else:
        print('NO')
#可以用内置函数来构造排列，（省的自己递归，而且时间更快）
from collections import defaultdict
from itertools import permutations

a = defaultdict(int)
b = defaultdict(int)
c = defaultdict(int)
d = defaultdict(int)
n = int(input())

for i in input():
    a[i] += 1
for i in input():
    b[i] += 1
for i in input():
    c[i] += 1
for i in input():
    d[i] += 1

dicts = [a, b, c, d]

def check(word):
    for perm in permutations(dicts, len(word)):
        for i, d in enumerate(perm):
            if word[i] not in d:
                break
        else:
            return 'YES'
    else:
        return 'NO'

for _ in range(n):
    word = input()
    print(check(word))




