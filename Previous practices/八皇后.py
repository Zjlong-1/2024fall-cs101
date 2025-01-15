#和深度优先搜索找出所有的路径的思想很像
#用一个列表来表示选择的状态！！！！！！！
l=[]
ans=[-1]*8
def a(ans,r,c):
    for i in range(r):
        if ans[i]==c:
            return False
        if abs(ans[i]-c)==abs(r-i):
            return False
    return True
def s(ans,r):
    if r==8:
        l.append(ans[:])
        return
    for c in range(8):
        if a(ans,r,c):
            ans[r]=c
            s(ans,r+1)
            ans[r]=-1
s(ans,0)
n=int(input())
for i in range(n):
    print(*[x+1 for x in l[int(input())-1]],sep='')







