from math import ceil

def perebor(fname: str) -> int:
    a = [0]*10_000
    with open(fname) as f:
        _, v = map(int, f.readline().split())
        for l in f:
            d, y = map(int, l.split())
            a[d] = ceil(y/v)
    
    mn = 10**15
    for i in range(len(a)):
        if a[i] == 0:
            continue
        current = 0
        for j in range(len(a)):
            current += abs(i - j) * a[j]
        mn = min(current, mn)
    return mn

def fast(fname: str) -> int:
    a = [0]*1_000_000
    with open(fname) as f:
        _, v = map(int, f.readline().split())
        for l in f:
            d, y = map(int, l.split())
            a[d] = ceil(y/v)
    
    left_partial_sum = [0] * len(a)
    left_partial_sum[0] = a[0]
    for i in range(1, len(left_partial_sum)):
        left_partial_sum[i] = left_partial_sum[i - 1] + a[i]
    right_partial_sum = [0] * (len(a) + 1)
    for i in reversed(range(len(right_partial_sum) - 1)):
        right_partial_sum[i] = right_partial_sum[i + 1] + a[i]
    
    lsum, rsum = 0, sum(right_partial_sum[1:])
    
    mn = 10**20
    for i in range(len(a)):
        mn = min(lsum + rsum, mn)
        lsum += left_partial_sum[i]
        rsum -= right_partial_sum[i + 1]
    return mn

# 1470813
print("А =", perebor("27.1.A.txt"))
print("A =", fast("27.1.A.txt"))
print("B =", fast("27.1.B.txt"))