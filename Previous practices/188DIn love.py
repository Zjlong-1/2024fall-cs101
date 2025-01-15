#考虑每一个操作使得区间上的每一个数加或减1，但单独弄会导致许多的空间开销，所以考虑用差分来表示
#但这就要求实现一个既有序又是字典集合，这显然是很难做到的。
#考虑一个点，有交集事实上只要保证leftmax>=rightmin(最难成的一对)就可以了
from collections import defaultdict
import heapq
n=int(input())
left=defaultdict(int)
right=defaultdict(int)
max1,min1=[],[]
for _ in range(n):
    a=input().split()
    l,r=int(a[1]),int(a[2])
    if a[0]=='+':
        left[l]+=1
        right[r]+=1
        heapq.heappush(max1,-l)
        heapq.heappush(min1,r)
    else:
        left[l] -= 1
        right[r] -= 1
    while max1 and left[-max1[0]]==0:
        heapq.heappop(max1)
    while min1 and right[min1[0]]==0:
        heapq.heappop(min1)
    if max1 and min1 and min1[0]<-max1[0]:
        print('Yes')
    else:
        print('No')