while True:
    n,p,m=map(int,input().split())
    if n==p==m==0:
        break
    l=[i for i in range(1,n+1)]
    k=[]
    while l:
        p=(p+m-1)%len(l)
        k.append(l[p-1])
        l.remove(l[p-1])
        if p==0:
            p=1
    print(*k,sep=',')

#测试了无数组数据才发现N时边界存在问题（太折磨了！！！！！）
#也可以1:1还原问题来做：
while True:
    n, p, m = map(int, input().split())
    if {n,p,m} == {0}:
        break
    monkey = [i for i in range(1, n+1)]
    for _ in range(p-1):
        tmp = monkey.pop(0)
        monkey.append(tmp)
    # print(monkey)

    index = 0
    ans = []
    while len(monkey) != 1:
        temp = monkey.pop(0)
        index += 1
        if index == m:
            index = 0
            ans.append(temp)
            continue
        monkey.append(temp)

    ans.extend(monkey)

    print(','.join(map(str, ans)))