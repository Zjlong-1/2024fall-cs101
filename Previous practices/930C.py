from collections import Counter
n=int(input())
l=list(map(int,input().split()))
l1=Counter(l)
print(l1.most_common(1)[0][1])
#计算最大频率即可（决定了有多少个单调序列）