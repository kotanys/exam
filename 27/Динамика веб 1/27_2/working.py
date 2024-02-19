file = open("27/Динамика веб 1/27_2_B.txt")
file.readline()
K = 79

current_sum = 0
sum_ost = [None] * K
len_ost = [None] * K
max_sum, max_len = 0, 0

for current_len, s in enumerate(file, start=1):
    current_sum += int(s)
    if current_sum % K == 0:
        max_sum = max(max_sum, current_sum)
        max_len = max(max_len, current_len)
    elif sum_ost[current_sum % K] != None:
        cut_sum = current_sum - sum_ost[current_sum % K]
        cut_len = current_len - len_ost[current_sum % K]
        max_sum = max(max_sum, cut_sum)
        max_len = max(max_len, cut_len)
    else:
        sum_ost[current_sum % K] = current_sum
        len_ost[current_sum % K] = current_len
print(max_len)