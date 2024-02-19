with open("") as file:
    _, k = map(int, file.readline().split())
    data = [int(s) for s in file]

mn_num9 = 10**10
for num9 in data:
    if '9' in str(num9) and num9 < mn_num9:
        mn_num9 = num9

min_pr = 10**10
for i in range(len(data)):
    for j in range(i + k, len(data)):
        for p in range(j + k, len(data)):
            if (data[i] + data[j] + data[p]) % mn_num9 == 0 \
                and (data[i] * data[j] * data[p]) < min_pr:
                min_pr = data[i] * data[j] * data[p]
print(min_pr)