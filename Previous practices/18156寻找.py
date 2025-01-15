t=int(input())
l=list(map(int,input().split()))
l.sort()
i=0
j=len(l)-1
n=len(l)
ans=float('inf')
while i<j:
    while i<j and l[i] + l[j] > t :
        j-=1
    if i!=j and ans>t-l[i]-l[j]:
        k=l[i]+l[j]
        ans=t-l[i]-l[j]
    if j<=n-2 and ans>l[i]+l[j+1]-t:
        k = l[i] + l[j+1]
        ans =l[i]+l[j+1]-t
    i+=1
    if j<n-1:
        j+=1
print(k)#想要省，却加大了许多思考量，反正要循环，不如多判断几下（减少分类与思考）
#改进！！！！！：
t = int(input())
l = list(map(int, input().split()))
l.sort()
i = 0
j = len(l) - 1
n = len(l)
closest_sum = float('inf')
best_sum = None
while i < j:
    current_sum = l[i] + l[j]
    if abs(current_sum - t) < abs(closest_sum - t):
        closest_sum = current_sum
        best_sum = current_sum
    elif abs(current_sum - t) == abs(closest_sum - t):
        best_sum = min(best_sum, current_sum) if best_sum is not None else current_sum
    if current_sum < t:
        i += 1
    else:
        j -= 1
print(best_sum)

