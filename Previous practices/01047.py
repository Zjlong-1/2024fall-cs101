while True:
    try:
        n=input()
        s=set()
        for i in range(len(n)):
            s.add(n[i:]+n[:i])
        t=True
        k=int(n)
        for i in range(len(n)):
            y=str(k*(i+1))
            if y not in s and '0'+y not in s:
                t=False
        if t:
            print(f'{n} is cyclic')
        else:
            print(f'{n} is not cyclic')
    except EOFError:
        break