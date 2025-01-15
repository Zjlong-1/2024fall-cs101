n=int(input())
l1=[]
l2=[]
for i in range(n):
    a,b=input().split('-')
    if a=='Bert':
        l1.append((b,float(b[:-1]),ord(b[-1])))
    else:
        l2.append((b,float(b[:-1]),ord(b[-1])))
l1.sort(key=lambda x:(-x[2],x[1]))
l2.sort(key=lambda x:(-x[2],x[1]))
print('Bert: '+', '.join(l1[i][0] for i in range(len(l1))))
print('GPT: '+', '.join(l2[i][0] for i in range(len(l2))))
#被题目坑了，不只有题干给的，有多个
from collections import defaultdict
n=int(input())
l=defaultdict(list)
for i in range(n):
    a,b=input().split('-')
    l[a].append((b,float(b[:-1]),ord(b[-1])))
l1=sorted(l)
for k in l1:
    l[k].sort(key=lambda x:(-x[2],x[1]))
    ka=', '.join(l[k][i][0] for i in range(len(l[k])))
    print(f'{k}: {ka}')
#字典排序后是列表！！！！！！！要小小拷贝一下（DEBUGE了很久都没发现）！！！！！
from collections import defaultdict
n=int(input())
l=defaultdict(list)
for i in range(n):
    a,b=input().split('-')
    l[a].append((b,float(b[:-1]),ord(b[-1])))
for k in sorted(l.keys()):
    l1=sorted(l[k],key=lambda x:(-x[2],x[1]))
    ka=', '.join(l1[i][0] for i in range(len(l1)))
    print(f'{k}: {ka}')
#好坑：l=sorted(l)  # l 返回的是一个列表，无法像字典那样使用 l[k]。
#用for k in sorted(l.keys()):来避免对字典的直接排序
#或者记住索引，拷贝：
sd = sorted(d)
#print(d)
for k in sd:
    paras = sorted(d[k],key=lambda x: x[1])
#将M和B进行转化：
from collections import defaultdict

n = int(input())
d = defaultdict(list)
for _ in range(n):
    #name, para = input().strip().split('-')
    name, para = input().split('-')
    if para[-1]=='M':
        d[name].append((para, float(para[:-1])/1000) )
    else:
        d[name].append((para, float(para[:-1])))


sd = sorted(d)
#print(d)
for k in sd:
    paras = sorted(d[k],key=lambda x: x[1])
    #print(paras)
    value = ', '.join([i[0] for i in paras])
    print(f'{k}: {value}')