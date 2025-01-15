n=int(input())
for i in range(n):
    k=0
    l=[]
    a=input()
    for m in a:
        if m!='0':#注意0的形式（字符串）
            k+=1
    print(k)
    for m in a:
        if m!='0':
            t=a.index(m)
            l.append(int(m)*(10**(len(a)-1-t)))
            a=str(int(a)-int(m)*(10**(len(a)-1-t)))#防止重复：每次均去除 ！
    print(*l)



#事实上，可以在遍历的时候就加上权重（位次）：
n = int(input("Enter the number of cases: "))
for _ in range(n):
    k = 0
    l = []
    a = input("Enter the number: ").strip()  # 读取输入并去除多余空格
    length = len(a)

    for m in a:
        if m != '0':  # 检查字符是否不是 '0'
            k += 1

    print(k)

    for i, m in enumerate(a):
        if m != '0':
            # 计算当前数字的权重并加入到列表中
            weight = int(m) * (10 ** (length - 1 - i))
            l.append(weight)

    print(l)


#更妙的想法：运用变化中的k(直接以此确定位置）
n = int(input())
for _ in range(n):
    s = input()
    cnt = 0
    res = []
    i = 0
    for c in s:
        i += 1
        if c != '0':
            cnt += 1
            res.append( int(c) * (10 ** (len(s) - i)) )
    print(cnt)
    print(*res)




