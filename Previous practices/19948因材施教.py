#转化为中间交汇点左减右最小
n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
l1=[l[i]-l[i+1] for i in range(n-1)]
l1.sort()
print(l[-1]-l[0]+sum(l1[0:m-1]))