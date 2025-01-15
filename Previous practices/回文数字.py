def solve(s):
    n=len(s)
    if n==1:
        return True
    left,right=0,n-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
while True:
    try:
        s=input()
        if solve(s):
            print('YES')
        else:
            print('NO')
    except EOFError:
        break

