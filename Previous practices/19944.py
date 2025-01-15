t=int(input())
for s in range(t):
    n = input()
    if n[4] == '0' and int(n[5])<=2 :
        m = 12 + int(n[5])
        k = int(n) // 10000 - 1
        n = int(n)
        y = k % 100
        c = k // 100
        d = n % 100
        w = (y + y // 4 + c // 4 - 2 * c + (26 * (m + 1)) // 10 + d - 1) % 7
    else:
        m = int(n[4]) * 10 + int(n[5])
        k = int(n) // 10000
        n = int(n)
        y = k % 100
        c = k // 100
        d = n % 100
        w = (y + y // 4 + c // 4 - 2 * c + (26 * (m + 1)) // 10 + d - 1) % 7
    l = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    print(l[w])




    #print(m,k,n,c,d,w),用于寻找错误



