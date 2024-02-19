def perebor(fname: str) -> int:
    with open(fname) as f:
        n = int(f.readline())
        a = list(map(int, f.readlines()))

    mx = 0
    for i in range(n):
        cur = 0
        for j in range(n):
            cur += abs(i - j) * a[j]
        mx = max(mx, cur)
    return mx

def fast(fname: str) -> int:
    with open(fname) as f:
        n = int(f.readline())
        a = list(map(int, f.readlines()))
    
    right_part_sum = [0] * (n + 1)
    right_part_sum[n - 1] = a[n - 1]
    for i in reversed(range(n - 1)):
        right_part_sum[i] = a[i] + right_part_sum[i + 1]
    
    left_part_sum = [0] * n
    left_part_sum[0] = a[0]
    for i in range(1, n):
        left_part_sum[i] = a[i] + left_part_sum[i - 1]
    
    mx = 0
    lsum = 0
    rsum = sum(right_part_sum[1:])
    for i in range(n):
        mx = max(mx, lsum + rsum)
        lsum += left_part_sum[i]
        rsum -= right_part_sum[i + 1]
    return mx

print(perebor("27A.txt"))
print(perebor("27A.txt"))
print(fast("27B.txt"))