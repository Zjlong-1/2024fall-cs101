l=input().split('+')
k=[int(i) for i in l ]
k.sort()
print(*k,sep='+')