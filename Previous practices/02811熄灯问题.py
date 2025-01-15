#注意到，在第一行开关灯确定之后，要想熄灯，那么后面n-1行的操作是固定的，所以只要枚举2**6次即可
#有问题同行之间的处理有问题,太麻烦了，不想改了，换一种方法
def z(a,b):
    result=~(int(a,2)^int(b,2))&0b111111
    return bin(result)[2:].zfill(6)
def z2(a,b):
    x=list(a)
    for i in range(1,5):
        if x[i]=='1' and b[i]=='1':
            x[i]='0'
        elif x[i]=='1' and b[i]=='0':
            x[i]

l=[input().split() for _ in range(5)]
light=[]
for i in range(5):
    light.append(''.join(l[i]))
for i in range(0,64):
    k=bin(i)[2:].zfill(6)
    def solve(light):
        ans=[k]
        light[0]=z(light[0],k)
        t=light[-1]
        for j in range(3):
            light[j+1]=z(light[j],light[j+1])
            light[j+2]=z(light[j],light[j+2])
            ans.append(light[j])
        if light[-1]==light[-2]:
            ans.append(light[-1])
            return True,ans
        else:return False,ans
    a,b=solve(light)
    if a:
        for x in b:
            print(x,sep=' ')
        break
# 先定义某个点的熄灯操作，反正就是一层一层，一次一次地操作
dx, dy = [0, 0, -1, 1, 0], [0, -1, 0, 0, 1]


def p(light, x, y):
    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 6:
            light[nx][ny] ^= 1


def solve():
    for j in range(64):
        s = [row[:] for row in light]
        solution = [[0] * 6 for _ in range(5)]
        for x in range(6):
            if (j >> x) & 1:
                solution[0][x] = 1
                p(s, 0, x)
        for i in range(1, 5):
            for j in range(6):
                if s[i - 1][j] == 1:
                    solution[i][j] = 1
                    p(s, i, j)
        if all(s[4][j] == 0 for j in range(6)):
            for i in solution:
                print(*i)


light = [[int(i) for i in input().split()] for _ in range(5)]
solve()



















