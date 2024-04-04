from math import ceil

CAPACITY = 47

f = open("Пробник/27A.txt")
f.readline()
a = [0] * 1000001
for line in f:
    d, v = map(int, line.split())
    a[d] = ceil(v / CAPACITY)
    
left_partial_sum = [0] * len(a)
for i in range(1, len(a)):
    left_partial_sum[i] = left_partial_sum[i - 1] + a[i]
    
right_partial_sum = [0] * len(a)
right_partial_sum[-1] = a[-1]
for i in reversed(range(0, len(a) - 1)):
    right_partial_sum[i] = right_partial_sum[i + 1] + a[i]
    
current = sum(right_partial_sum[1:])
mn = current
best = 1
for i in range(1, len(right_partial_sum)):
    current += left_partial_sum[i - 1]
    current -= right_partial_sum[i]
    if current < mn:
        mn = current
        best = i
print(best,mn)