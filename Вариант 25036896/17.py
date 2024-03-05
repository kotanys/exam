with open("Вариант/17.txt") as f:
    a = list(map(int, f.readlines()))

max17 = max(filter(lambda x: x % 17 == 0, a))

cnt = 0
mx = -1
for i in range(len(a) - 1):
    if a[i] + a[i + 1] > max17:
        cnt += 1
        mx = max(mx, a[i] + a[i + 1])
print(cnt, mx)