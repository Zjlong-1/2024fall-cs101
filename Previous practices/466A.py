n,m,a,b=map(int,input().split())
t=n//m
if b<=m*a:
   print(min((t*b+(n%m)*a),t*b+b))
else:
    print(n*a)


#看似十分简单，但实际上存在坑点：可以买特价票并不用玩
#而且特价票不一定真的是特价！

