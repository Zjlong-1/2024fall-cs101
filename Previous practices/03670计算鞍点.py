l=[list(map(int,input().split())) for _ in range(5)]
l1=[[0]*5 for i in range(5)]
for i in range(5):
    m=l[i][0]
    l1[i][0]=1
    t=0
    for j in range(1,5):
        if l[i][j]>m:
            m=l[i][j]
            l1[i][j]+=1
            l1[i][t]-=1
            t=j
for j in range(5):
    m=l[0][j]
    l1[0][j]=1
    t=0
    for i in range(1,5):
        if l[i][j]<m:
            m=l[i][j]
            l1[i][j]+=1
            l1[t][j]-=1
            t=i
ans=False
for i in range(5):
    for j in range(5):
        if l1[i][j]==2:
            print(f'{i+1} {j+1} {l[i][j]}')
            ans=True
            break
if not ans:
    print('not found')
#量级比较小，可以用sum和index
l = [list(map(int, input().split())) for _ in range(5)]
ans = False
for i in range(5):
    max_val = max(l[i])
    col_index = l[i].index(max_val)
    is_saddle_point = True
    for k in range(5):
        if l[k][col_index] < max_val:
            is_saddle_point = False
            break
    if is_saddle_point:
        print(f'{i + 1} {col_index + 1} {max_val}')
        ans = True
        break
if not ans:
    print('not found')
