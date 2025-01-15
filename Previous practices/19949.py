n=int(input())
k=0
for i in range(n):
    l=input().split()
    for p in range(len(l)):
        if len(l[p])>=6:
            if  l[p][0]==l[p][1]==l[p][2]==l[p][-1]==l[p][-2]==l[p][-3]=='#':
                k+=1
    for p in range(len(l)-1):
        if len(l[p])>=6 and len(l[p+1])>=6:
            if  l[p][0]==l[p][1]==l[p][2]==l[p][-1]==l[p][-2]==l[p][-3]==l[p][0]==l[p+1][1]==l[p+1][2]==l[p+1][-1]==l[p+1][-2]==l[p+1][-3]=='#':
                k=k-1
print(k)
#事实上，本题可以钻漏洞：即除了用来表示实体，其余的不会存在#。这是因为是英语句子。而且单词也不会有
#l[p][0]==l[p][1]==l[p][2]==l[p][-1]==l[p][-2]==l[p][-3]这中形式，所以是否等于#都无所谓
#也可以只去除连着的6个#，再数连着的3#个数除以2即可（//2）
T = int(input())
ans = 0
while T>0:
    T -= 1
    ans += (input().replace('### ###', '')).count('###') // 2
print(ans)

#另一种比较强的方法：
n = int(input())

cnt = 0
for _ in range(n):
    s = input()
    s = s.replace(r"### ###", " ")
    # print(s)
    while True:
        begin = s.find("###")
        if begin == -1: break

        end = s.find("###", begin + 3)

        cnt += 1
        s = s[end + 3:]

print(cnt)
