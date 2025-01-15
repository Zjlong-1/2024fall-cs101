while True:
    try:
        n=int(input())
        l = list(map(int, input().split()))
        l.sort()
        s=sum(l)
        maxl=max(l)
        if s>=maxl*2:
            print(f'{s/2:.1f}')
        else:
            print(f'{s-maxl:.1f}')
    except EOFError:
        break



