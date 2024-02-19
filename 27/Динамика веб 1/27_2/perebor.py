file = open("27/Динамика веб 1/27_2_A.txt")
file.readline()
K = 79

data = [int(s) for s in file]
max_sum, max_len = 0, 0

for i in range(len(data)):
    for j in range(i, len(data)):
        current_sum = sum(data[i:j + 1])
        if current_sum % K == 0:
            max_sum = max(current_sum, max_sum)
            max_len = max(max_len, j + 1 - i)
print(max_len)