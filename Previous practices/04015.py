while True:
    try:
        n =input()
    except EOFError:
        break

    if n.count('@') != 1:
        print('NO')
    elif n[0] == '@' or n[0] == '.' or n[-1] == '.' or n[-1] == '@':
        print('NO')
    elif '@.' in n or '.@'in n:
        print('NO')
    else:
        z = n.find('@')
        o = 0
        for i in range(z, len(n)):#可以改进：for i in n[z:]
            if n[i] == '.':
                o = 1
        if o == 1:
            print('YES')
        else:
            print('NO')








