n=int(input())
for i in range(n):
    l=[]
    l1=[]
    l2=[]
    for i in range(3):
        a,b,c=input().split()
        if c=='even':
            for k in range(4):
                l.append(a[k])
                l.append(b[k])
        else:
            l2.append((a,c))
            for k in range(4):
                l1.append(a[k])
                l1.append(b[k])
for i in l1:
    if i not in l:
        if i in l2[0][0] and l2[0][1]=='up':
            print(i+' '+'is the counterfeit coin and it is heavy.')
        if i in l2[0][0] and l2[0][1] == 'down':
            print(i+' '+'is the counterfeit coin and it is light.')
        if i not in l2[0][0] and l2[0][1] == 'down':
            print(i + ' ' + 'is the counterfeit coin and it is heavy.')
        if i not in l2[0][0] and l2[0][1] == 'up':
            print(i + ' ' + 'is the counterfeit coin and it is light.')
#好坑，天平不一定放四个。枚举显然会累死，所以只研究假币的性质。
n=int(input())
for y in range(n):
    l = [[], [], []]
    for i in range(3):
        l[i] = input().split()
    for k in 'ABCDEFGHIJKL':
        if all((k in i[0] and i[2] == 'up') or (k in i[1] and i[2] == 'down') or (k not in i[0]+i[1] and i[2] == 'even')  for i in l):
            print('{} is the counterfeit coin and it is {}.'.format(k, 'heavy'))
        if all((k in i[0] and i[2] == 'down') or (k in i[1] and i[2] == 'up') or (k not in i[0]+i[1] and i[2] == 'even') for i in l):
            print('{} is the counterfeit coin and it is {}.'.format(k, 'light'))


