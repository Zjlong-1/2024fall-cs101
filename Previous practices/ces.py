word1=input()
word2=input()
n, m = len(word1), len(word2)
la = [[max(m,n)] * m for _ in range(n)]
s = set(word1[0])
s1 = set()
for i in range(m):
    s1.add(word2[i])
    if word1[0] in s1:
        la[0][i] = i
    else:
        la[0][i] = i + 1
for i in range(1, n):
    s.add(word1[i])
    if word2[0] in s:
        la[i][0] = i
    else:
        la[i][0] = i + 1
    for j in range(1, m):
        if word1[i] == word2[j]:
            la[i][j] = la[i - 1][j - 1]
        else:
            la[i][j] = min(la[i - 1][j], la[i][j - 1], la[i - 1][j - 1]) + 1
print(la[-1][-1])




