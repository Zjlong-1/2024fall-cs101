#while True:
#   l=list(map(int,input().split()))
#    a=0
 #   if l[4]>0:
  #      if l[0]>11*l[4]:
   #         l[0]=l[0]-11*l[4]
    #    else:
     #       l[0]=0
 #       a+=l[4]
  #  if l[3]>0:
   #     l[3]=l[3]%4
    #    t=l[3]
     #   a+=l[3]//4
      #  if t==1:
       #     if l[]
#分类分麻了！借鉴一下思路:先确定大致的装箱数，再将1,2填入其中
import math

while True:
    a, b, c, d, e, f = map(int, input().split())
    if a + b + c + d + e + f == 0:
        break
    t = d + e + f
    l = [0, 5, 3, 1]
    bb = 5 * d + l[c % 4]
    t += math.ceil(c / 4)
    if b > bb:
        t += math.ceil((b - bb) / 9)
    aa = 36 * t - 36 * f - 25 * e - 16 * d - 9 * c - 4 * b
    if a > aa:
        a = a - aa
        t += math.ceil(a / 36)
    print(t)
#非常非常困难的一道题，不仅容易陷入分类的苦海，还很考察思维的严谨先确定大概再用填补法处理


