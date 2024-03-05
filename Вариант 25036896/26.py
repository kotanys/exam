with open("Вариант 25036896/26.txt") as f:
    s, n = map(int, f.readline().split())
    a = list(map(int, f.readlines()))
    
a.sort(reverse=True)
got = []
current = 0
l, r = 0, len(a) - 1
is_largest = True
while current + a[r] <= s:
    if is_largest:
        while current + a[l] > s:
            l += 1
        got.append(a[l])
        current += a[l]
        l += 1
    else:
        while current + a[r] > s:
            r -= 1
        got.append(a[r])
        current += a[r]
        r -= 1
    is_largest = not is_largest
print(len(got), got[-1])