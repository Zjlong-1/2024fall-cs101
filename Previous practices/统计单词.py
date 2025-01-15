import sys
import re
s=set()
s1={}
l=sys.stdin.read()
l1=words = re.findall(r"\b\w+(?:'\w+)?\b",l)
for i in l1:
    if i in s:
        s1[i] += 1
    else:
        s.add(i)
        s1[i] = 1
for a in s1:
    print(a,s1[a])
#不仅可以是句号，逗号，还可以是其他符号，很坑。
