#n=input()
#m=input()
#if len(n)==len(m):
#    l=[0]*(len(n)+1)
#    for i in range(len(n),-1,-1):
#        l[i]=(int(m[i-1])+int(n[i-1]))%10
#        l[i-1]+=(int(m[i-1])+int(n[i-1]))//10
#if len(n)>len(m):
#    l=[0]*(len(n)+1)
#    for i in range(-1,-len(m),-1):
#        l[i]=(int(m[i-1])+int(n[i-1]))%10
 #       l[i-1]+=(int(m[i-1])+int(n[i-1]))//10
  #  for i in range(-len(m),-len(n)-2,-1):
  #      l[i]=l[i]%10
   #     l[i-1]=l[i-1]+l[i]//10
#if
#my简化版：
    n = input()
    m = input()
    if len(n) < len(m):
        n, m = m, n
    l = [0] * (len(n) + 1)
    for i in range(-1, -len(m) - 1, -1):
        l[i - 1] += (int(m[i]) + int(n[i]) + l[i]) // 10
        l[i] = (l[i] + int(m[i]) + int(n[i])) % 10
    for i in range(-len(m) - 1, -len(n) - 1, -1):
        l[i - 1] += (l[i] + int(n[i])) // 10
        l[i] = (l[i] + int(n[i])) % 10
    while int(l[0]) == 0 and len(l) > 1:
        l = l[1:]
    print(*l, sep='')
    # 按照加法原理定义即可,但很考验思维的完备性,检验了一遍又一遍！




