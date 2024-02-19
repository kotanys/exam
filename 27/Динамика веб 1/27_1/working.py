from math import ceil, sqrt
def is_prime(x):
    for div in range(2, ceil(sqrt(x))):
        if x % div == 0:
            return 0
    return 1 if (x >= 2) else 0

K = 7
current_sum = 0
current_prime_cnt = 0
sum_ost = [None] * K
cnt_prime_ost = [None] * K
max_sum = -1

file = open("27/Динамика веб 1/27_1_A.txt")
file.readline()
for s in file:
    current_sum += int(s)
    current_prime_cnt += is_prime(int(s))
    if current_prime_cnt % K == 0:
        max_sum = max(max_sum, current_sum)
    elif cnt_prime_ost[current_prime_cnt % K] != None:
        cut_sum = current_sum - sum_ost[current_prime_cnt % K]
        max_sum = max(max_sum, cut_sum)
    else:
        cnt_prime_ost[current_prime_cnt % K] = current_prime_cnt
        sum_ost[current_prime_cnt % K] = current_sum
print(max_sum)