t=int(input())
for _ in range(t):
    n,x,y,h=map(int,input().split())
    l=[]
    for i in range(n):
        a,b,c=map(int,input().split())
        l.append((a,b,c))
    l.append((0,0,0))
    l.append((x,x,y))
    l.sort(key=lambda x: x[2])
    laleft=[float('inf')]*(n+2)
    laright=[float('inf')]*(n+2)
    for i in range(1,n+2):
        for j in range(i-1,-1,-1):
            if l[i][2]-l[j][2]>h:
                break
            if j==0 :
                laleft[i]=0
                break
            if l[j][0]<=l[i][0]<=l[j][1] :
                laleft[i]=min(laleft[j]-l[j][0]+l[i][0],laright[j]-l[i][0]+l[j][1])
                break
        for j in range(i-1,-1,-1):
            if l[i][2]-l[j][2]>h:
                break
            if j==0 :
                laright[i]=0
                break
            if l[j][0]<=l[i][1]<=l[j][1] :
                laright[i]=min(laleft[j]-l[j][0]+l[i][1],laright[j]-l[i][1]+l[j][1])
                break
    print(min(laleft[n+1],laright[n+1])+y)
#这个代码是联想数字三角形而形成的，由底部到顶部，不断进行。
#被一个小条件坑了：如果Jimmy恰好落在某个平台的边缘，被视为落在平台上。独立敲出超过1000的代码！！！！！
#当然也可以用DFS：
from collections import deque, defaultdict


def min_time_to_ground(t, test_cases):
    results = []
    for case in test_cases:
        N, X, Y, MAX, platforms = case
        platforms.append((-float('inf'), float('inf'), 0))  # 添加地面平台，高度为0，长度无限

        platforms.sort(key=lambda p: p[2], reverse=True)  # 按高度从高到低排序
        min_time = defaultdict(lambda: float('inf'))  # 保存每个平台的最小时间
        min_time[(X, Y)] = 0  # 初始位置的时间为0

        queue = deque([(X, Y, 0)])  # 初始位置加入队列

        while queue:
            x, y, time = queue.popleft()

            # 找到落脚的目标平台
            for x1, x2, h in platforms:
                if h >= y:  # 不能下落到更高的平台
                    continue
                if abs(y - h) > MAX:  # 如果下落高度超过MAX，跳过
                    continue
                if x1 <= x <= x2:  # 如果目标平台可以落脚
                    fall_time = time + (y - h)  # 计算下落时间

                    # 到达地面
                    if h == 0:
                        results.append(fall_time)
                        break

                    # 向左跑到边缘
                    if fall_time + (x - x1) < min_time[(x1, h)]:
                        min_time[(x1, h)] = fall_time + (x - x1)
                        queue.append((x1, h, fall_time + (x - x1)))

                    # 向右跑到边缘
                    if fall_time + (x2 - x) < min_time[(x2, h)]:
                        min_time[(x2, h)] = fall_time + (x2 - x)
                        queue.append((x2, h, fall_time + (x2 - x)))
            else:
                continue
            break

    return results


# 输入处理
t = int(input())
test_cases = []
for _ in range(t):
    first_line = list(map(int, input().split()))
    N, X, Y, MAX = first_line
    platforms = [tuple(map(int, input().split())) for _ in range(N)]
    test_cases.append((N, X, Y, MAX, platforms))

# 计算结果并输出
results = min_time_to_ground(t, test_cases)
for res in results:
    print(res)



