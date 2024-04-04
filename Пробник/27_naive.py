from math import ceil

CAPACITY = 47

f = open("Пробник/27A.txt")
f.readline()
a = [0] * 1001
for line in f:
    d, v = map(int, line.split())
    a[d] = ceil(v / CAPACITY)

mn = 10**10
best = -1
for i in range(len(a)):
    cur = 0
    for j in range(len(a)):
        cur += abs(i - j) * a[j]
    if cur < mn:
        best = i
        mn = cur
print(best)