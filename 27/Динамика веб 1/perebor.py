file = open("27/Динамика веб 1/27_3_A.txt")
_, k = map(int, file.readline().split())
data = [int(s) for s in file]

min_len, min_sum = 10**10, 10**10
for i in range(len(data)):
    for j in range(i + k - 1, len(data)):
        cut = data[i:j + 1]
        sum_cut = sum(cut)
        len_cut = j + 1 - i
        if sum_cut % 252 == 0:
            if len_cut <= min_len:
                min_len = len_cut
                min_sum = sum_cut
            if min_len == len_cut and sum_cut < min_sum:
                min_sum = sum_cut
print(min_sum)