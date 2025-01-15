n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
k=input()
t=0
l1=sorted(l,key=lambda x:(x[0],x[1]) ,reverse=True)
l2=sorted(l,key=lambda x:(x[1],-x[0]))
for i in range(n):
    if l1[i]==l2[i]:
        t+=1
print(t)
#事实上，也是找到顺序对个数，但这里有坑。即距离or价格可能相等，需要采用数对第1,2个均排列的方法
#由于这个天坑，以及收尾必是的性质，使得这种方法寸步难行
while True:
    N = int(input())
    if N == 0:
        break
    l=[]
    for _ in range(N):
        D, C = map(int, input().split())
        l.append((D, C))
    l.sort(key=lambda x: (x[0],x[1]))
    a= 0
    t= float('inf')
    for D, C in l:
        if C <t:
            a += 1
            t=C
    print(a)
#任何比 M 更靠近海边的酒店都将比 M 贵。任何比 M 便宜的酒店都比 M 离海边更远。看似两个条件，但事实上，要换一种角度考虑：比他贵的不需要管，只要比他便宜的都比他远即可
#这样只需反向排序即可
#或者可以考虑比他近的全都比他贵即可，满足条件的数组会小于之前min,因此只需递归即可。
