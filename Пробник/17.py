f = open('Пробник/1.txt')
a = list(map(int, f.readlines()))
f.close()
mx = max(x for x in a if x % 22 == 0)
cnt = 0
mx_sum = -10**10
for i in range(len(a) - 1):
    if (a[i] < mx and a[i + 1] < mx) and (a[i] % 13 == 0 or a[i + 1] % 13 == 0):
        cnt += 1
        mx_sum = max(mx_sum, a[i] + a[i + 1])
print(cnt, mx_sum)