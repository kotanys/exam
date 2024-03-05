with open("17a.txt") as f:
    a = [int(s) for s in f]

min_pair_sum = 10**10
for i in range(len(a) - 1):
    min_pair_sum = min(min_pair_sum, a[i] + a[i + 1])
    
def has_c_in_15cc(num):
    while num != 0:
        if num % 15 == 12:
            return True
        num //= 15
    return False

cnt = 0
max_sum = 0
for i in range(len(a) - 4):
    subs = (a[i], a[i + 2], a[i + 4])
    cond1 = any(has_c_in_15cc(x) for x in subs)
    cond2 = min(subs)**0.5 > min_pair_sum
    if cond1 and cond2:
        cnt += 1
        max_sum = max(sum(subs), max_sum)
print(cnt, max_sum)