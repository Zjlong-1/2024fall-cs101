import re
k = {'1','2', '3', '4', '5', '6', '7', '8', '9','0'}
def a(x):
    i=len(x)-1
    t=0
    while x[i]  in k:
        i-=1
    for j in range(i+1):
        t+=(26**(i-j))*(ord(x[j])-64)
    print(f'R{x[i+1:]}C{t}')
def b(x):
    r, c = map(int, x[1:].split('C'))
    res=''
    while c:
        c, remainder = divmod(c - 1, 26)
        res = chr(65 + remainder) + res
    print(f'{res}{r}')
n=int(input())
for _ in range(n):
    x=input()
    if re.match(r'R\d+C\d+', x):
        b(x)
    else:
        a(x)
#原本蹩脚的解法：
# i = 1
#while x[i] in k:
 #   i += 1
#t1 = x[1:i]
#t2 = x[i + 1:len(x)]
#标答：
import re
def solve(s):
    if re.match(r'R\d+C\d+', s):
        r, c = map(int, s[1:].split('C'))
        res = ''
        while c:
            c, remainder = divmod(c - 1, 26)
            res = chr(65 + remainder) + res
        return res + str(r)
    else:
        pos = 0
        while not s[pos].isdigit():
            pos += 1
        res = 'R' + s[pos:] + 'C'
        c = 0
        for ch in s[:pos]:
            c = c * 26 + ord(ch) - 64
        return res + str(c)

n = int(input().strip())
for _ in range(n):
    s = input().strip().split('\n')[0]
    print(solve(s))



