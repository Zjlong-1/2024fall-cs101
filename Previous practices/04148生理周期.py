k=0
while True:
    k+=1
    a,b,c,d=map(int,input().split())
    if a==b==c==d==-1:
        break
    t=0
    while (t+d-a)%23!=0 or (t+d-b)%28!=0 or (t+d-c)%33!=0 or t==0:
        t+=1
    print('Case {}: the next triple peak occurs in {} days.'.format(k,t))
#优化：

m=1
while True:
    p,e,i,d-map(int,input().split())
    if p==-1:
        break
    n=0
    #加上定义，略
    dp=[O]*(d+21253) for x in range(p,d+21253,23):
    dp[x]+=1
    for x in range(e,d+21253,28):
        dp[x]+=1
    for x in range(i,d+21253,33):
        dp[x]+=1
    if dp[x]==3 and x!=0:
         n=x
         break
print(f"Case {m}: the next triple peak occurs in {n-d} days.") m+=1