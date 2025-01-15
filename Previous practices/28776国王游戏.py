n=int(input())
a,b=map(int,input().split())
l=[]
for _ in range(n):
    x,y=map(int,input().split())
    l.append((x,y))
from functools import cmp_to_key
def compare(a1, b1, a2, b2):
    return (max(1 / b1, a1 / b2) >= max(1 / b2, a2 / b1)) - \
           (max(1 / b1, a1 / b2) < max(1 / b2, a2 / b1))
def compare_wrapper(x, y):
    return compare(x[0], x[1], y[0], y[1])
l = sorted(l, key=cmp_to_key(compare_wrapper))
ans=a//l[0][1]
for i in range(1,n):
    a*=l[i-1][0]
    b*=l[i-1][1]
    ans=max(ans,a//l[i][1])
print(ans)
#两个连续的数组之间谁排前面可以由一个函数决定，以此函数排序在以此更新最大值
#还可以再优化，1/b1<a2/b1 and 1/b2<a1/b2 事实上只需比较a2/b1和a1/b2
#即只需比较a1*b1 and a2*b2即可
"""
直接想很难想到贪心策略，不妨逆推一下，我们先假设有了一个排列，然后看怎么换排列中大臣的顺序能得到更优的结果

首先，交换第i个大臣和第j个大臣(i<j)，不会影响1~i-1中的大臣的结果和第j+1~n中的大臣的结果
设1到i-1所有大臣的左手的乘积为x_1(包括国王)，i+1到j-1中所有大臣的左手乘积为x_2，第i个大臣右手的数为r_i,左手为l_i，第j个大臣右手的数为r_j左手为l_j。
不交换i和j:
第i个大臣获得金币:w_1[i] = x_1 / r_i
第j个大臣获得金币:w_1[j] = x_1 * x_2 * l_i / r_j
ans = max(ans, w_1[i], w_1[j])
交换i和j:
第i个大臣获得金币:w_2[i] = x_1 * x_2 * l_j / r_i
第j个大臣获得金币:w_2[j] = x_1 / r_j
ans = max(ans, w2[i], w2[j])
显然w_2[i]>w_1[i], w_1[j]>w_2[j]
ans = max(ans, w_2[i],w_1[j])

若w_1[j]>w_2[i](即此时要交换i和j,才能得到ans最优情况,取w_2[i]而不是w1[j]):
化简可得l_i * r_i > l_j * r_j
也就是说，当一个大臣左右手乘积>后面的大臣的左右手乘积时,交换这两个大臣，可以得到最大答案的最小值。
"""
from typing import List
def Solution(n:int, a:int, b:int, lst:List[List]) -> int:
    lst.sort(key=lambda x: (x[0] * x[1]))
    ans = 0
    for i in range(n):
        ans = max(ans, a // lst[i][1])
        a *= lst[i][0]
    return ans
if __name__ == "__main__":
    n = int(input())
    a, b = map(int, input().split())
    lst = []
    for i in range(n):
        lst.append([int(_) for _ in input().split()])
    # 时间复杂度O(nlogn)，空间复杂度O(n)

    print(Solution(n, a, b, lst))