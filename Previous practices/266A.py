n = int(input())
s = input()

m = 0
for i in range(n - 1):
    if s[i] == s[i + 1]:
        m += 1

print(m)

