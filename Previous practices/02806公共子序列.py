#用动态规划，l[i][j]表示两个序列以第i,j个结尾时的公共长度，为避免更新的数据干扰，可以j逆循环。
while True:
    try :
        a,b=input().split()
    except EOFError:
        break
    la=[[0]*len(b) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)-1,-1,-1):
            if a[i]==b[j]:
                if i==0 or j==0:
                    la[i][j]=1
                else:
                    la[i][j]=max(la[x][y] for x in range(i) for y in range(j))+1
    print(max(la[x][y] for x in range(len(a)) for y in range(len(b))))
#显然超时了，max用太多次了。
#换DP意义，即前i,j个的最大公共数,找一个更大的切入点（整体讨论，减少循环）
while True:
    try:
        a, b = input().split()
    except EOFError:
        break
    la = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                la[i][j] = max(la[i - 1][j - 1] + 1,la[i - 1][j], la[i][j - 1])
            else:
                la[i][j] = max(la[i - 1][j], la[i][j - 1])
    print(la[len(a)][len(b)])
