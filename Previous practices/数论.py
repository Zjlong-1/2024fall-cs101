def pFactors(n):
    """Finds the prime factors of 'n'"""
    from math import sqrt
    pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n

    for check in range(2, limit):
        while num % check == 0:
            pFact.append(check)
            num /= check
    if num > 1:
        pFact.append(num)
    return pFact
n=int(input())
l=pFactors(n)
if n==1:
    print(1)
else:
    for i in l:
        if l.count(i) >= 2:
            print(0)
            break
        elif len(l) % 2 == 0:
            print(1)
            break
        else:
            print(-1)
            break





