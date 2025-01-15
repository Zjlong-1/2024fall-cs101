n=int(input())
l=[]
a=0
for i in range(1,n+1):
    k=i%10
    p=i%70
    if i%7==0 :
        a=0
    elif k==7 or p<=9 and i>9:
        a=0
    else:
        l.append(i)
print(sum(k**2 for k in l))
print(l)
#事实上，这里把1-9给排出去了，我也不太想思考了，所以直接枚举加上去了。但当输出小于10的数时就会出现bug
#所以我又加了大于9的范围