n=int(input())
for i in range(2,n+1):
    for j in range(i,n+1):
        for k in range(j,n+1):
            a=i**3+j**3+k**3
            if (a**(1/3))**3==a and a<=n**3 :
                print("Cube ={} , Triple = ({},{},{})".format(int(a**(1/3)),i,j,k))
#优化：
n = int(input())
for i in range(2, n + 1):
    a_cubed = i ** 3
    for j in range(2, n + 1):
        for k in range(j, n + 1):
            for l in range(k, n + 1):
                if a_cubed == (j ** 3 + k ** 3 + l ** 3):
                    print("Cube = {}, Triple = ({}, {}, {})".format(i, j, k, l))
#再优化，将所有立方数存入列表，在引用即可
n = int(input())
l1=[i**3 for i in range(101)]
for i in range(2, n + 1):
    a_cubed = l1[i]
    for j in range(2, n + 1):
        for k in range(j, n + 1):
            for l in range(k, n + 1):
                if a_cubed == l1[j]+l1[k]+l1[l]:
                    print("Cube = {}, Triple = ({},{},{})".format(i, j, k, l))
#还可以再简化:1.将101改为n+1（可以在一些情况下简化）
#           2.用in来判断A是否为立方数
