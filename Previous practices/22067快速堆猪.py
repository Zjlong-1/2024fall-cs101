stack=[]
while True:
    try:
        l=input().split()
        if len(l)==2:
            min1=int(l[1])
            stack.append(min1)
            break
    except EOFError:
        break
while True:
    try:
        l=input().split()
    except EOFError:
        break
    if l[0]=='min' and stack :
        print(min1)
    elif l[0]=='push':
        stack.append(int(l[1]))
        min1,min2=min(min1,int(l[1])),max(min1,int(l[1]))
        break
    elif stack :
        k=stack.pop()
        min1=float('inf')
#思路有问题，过不了。每次push时，在辅助栈中加入当前最轻的猪的体重，pop时也同步pop，这样栈顶始终是当前猪堆中最轻的体重，查询时直接输出即可
#被提示坑了，不是单调栈（Pop多次），而是简单的记录栈(地下的最小）
s1,s2=[],[]
while True:
    try:
        l=input().split()
    except EOFError:
        break
    if l[0]=='pop' and s1:
        s1.pop()
        s2.pop()
    elif l[0]=='min' and s2:
        print(s2[-1])
    elif l[0]=='push':
        k=int(l[1])
        s1.append(k)
        if s2:
            s2.append(min(s2[-1],k))
        else:
            s2.append(k)



