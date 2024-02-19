file = open("27/Динамика веб 1/27_3_A.txt")
_, k = map(int, file.readline().split())

D = 252

current_sum = 0
sum_ost = [None] * D
len_ost = [None] * D
min_sum, min_len = 10**10, 10**10

for current_len, s in enumerate(file, start=1):
    current_sum += int(s)
    if current_sum % D == 0 and current_len >= k:
        if current_len <= min_len:
            min_len = current_len
            min_sum = current_sum
        if current_len == min_len and current_sum < min_sum:
            min_sum = current_sum
    elif len_ost[current_sum % D] != None:
        cut_len = current_len - len_ost[current_sum % D]
        if cut_len < k:
            continue
        cut_sum = current_sum - sum_ost[current_sum % D]
        if cut_len <= min_len:
            min_len = cut_len
            min_sum = cut_sum
        if cut_len == min_len and cut_sum < min_sum:
            min_sum = cut_sum
    
    sum_ost[current_sum % D] = current_sum
    len_ost[current_sum % D] = current_len
print(min_sum)