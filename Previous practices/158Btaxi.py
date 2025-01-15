from math import(ceil)
n=int(input())
l=list(map(int,input().split()))
t=l.count(4)+l.count(3)+ceil(l.count(2)/2)
k1=l.count(3)+2*(l.count(2)%2)
if l.count(1)>k1:
    print(t+ceil((l.count(1)-k1)/4))
else:
    print(t)
#若觉得count多次很费时，可以用collection函数中的Counter,只需计算一次
#from collections import Counter
#后面的l.count()改为l1[]即可
