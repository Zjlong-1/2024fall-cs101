n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    l1=[min(a-k,k) for k in l]
    print(max(l1),a-min(l1))
#做这道题的感悟颇深：最小是简单的，只要让最中间的正常走完即可。而对于最久的情况，一开始卡在碰来碰去的思考上，根本无法理清。后来问了GPT，他说只要算单个最远即可。
#这就给我打开了思路，考虑相遇的两个蚂蚁，他们的运动时间相同，顾运动路程也相同，相遇后反向，可以理解为交换。但事实上，两者的轨迹图的和没有变，而且路程只是进行了交换（与不撞相比），即路程的集合没变。
#由于是考虑整体，所以可以认为是相遇后不变方向，这时只要考虑单个的运动最长时间即可。