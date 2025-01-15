def can_light_room(vertices):
    x_coords = [x for x, y in vertices]
    y_coords = [y for x, y in vertices]
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)
    room_area = (max_x - min_x) * (max_y - min_y)
    polygon_area = 0
    n = len(vertices)
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        polygon_area += x1 * y2 - x2 * y1
    polygon_area = abs(polygon_area) / 2
    if polygon_area == room_area:
        return "Yes"
    else:
        return "No"
while True:
    n = int(input())
    if n == 0:
        break
    vertices = [tuple(map(int, input().split())) for _ in range(n)]
    print(can_light_room(vertices))
#gpt的算法有误，事实上，只要考虑是否可以照亮每一个边即可。
while True:
    n=int(input())
    if n==0:
        break
    l=[tuple(map(int,input().split())) for _ in range(n)]
    minx,miny,maxx,maxy=-float('inf'),-float('inf'),float('inf'),float('inf')
    for i in range(n):
        j=(i+1)%n
        if l[i][0] == l[j][0]:
            if l[i][1] < l[j][1]:
                minx = max(minx, l[i][0])
            else:
                maxx = min(maxx, l[i][0])
        else:
            if l[i][0] < l[j][0]:
                maxy = min(maxy, l[i][1])
            else:
                miny = max(miny, l[i][1])
    if minx <= maxx and miny <= maxy:
        print("Yes")
    else:
        print("No")
