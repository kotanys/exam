DIVLIMIT = 25
PATH = "C:\\Users\\Пользователь\\OneDrive\\ЕГЭ\\Статград ИН2210401\\files\\27-B.txt"

k = [[0]*DIVLIMIT for _ in range(DIVLIMIT)]
with open(PATH) as file:
    file.readline()
    for line in file:
        x = int(line)
        by2, by5 = 0, 0
        while x % 2 == 0:
            by2 += 1
            x //= 2
        while x % 5 == 0:
            by5 += 1
            x //= 5
        k[by2][by5] += 1

ans = 0
for i in range(DIVLIMIT):
    for j in range(DIVLIMIT):
        for p in range(DIVLIMIT):
            for q in range(DIVLIMIT):
                if (i + p >= 7 and j + q >= 7) and (i + p == 7 or j + q == 7):
                    if i == p and j == q:
                        ans += k[i][j] * (k[i][j] - 1)
                    else:
                        ans += k[i][j] * k[p][q]
ans //= 2
print(ans)