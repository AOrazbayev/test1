n = int(input())

m = []

for i in range(n):
    m.append(input().split())

s1 = 0
for i in range(n):
    s1 += int(m[i][i])
s2 = 0
for i in range(n):
    s2 += int(m[n-1-i][i])
if s2 != s1:
    print('NO')
    exit()

for j in range(n):
    s = 0
    for i in range(n):
        s += int(m[i][j])
    if s != s1:
        print('NO')
        exit()

for i in range(n):
    s = 0
    for j in range(n):
        s += int(m[i][j])
    if s != s1:
        print('NO')
        exit()

print('YES')