while True:
    w, h = map(int, input().split())
    if w==h==0:
        break
    l = [input() for i in range(h)]
    while True:
        a,b,c,d=map(int,input().split())
        if a==b==c==d==0:
            break
        
