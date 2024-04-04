distances = [388, 485, 162, 222, 50, 4, 16, 65]

for d in distances:
    if d % 4 == 0 and d % 6 != 0:
        print(d, "\tзелёная")
        continue
    divcnt = 0
    for div in range(2, d):
        if d % div == 0:
            divcnt += 1
    if divcnt == 2:
        print(d, "\tжёлтая")
        continue
    print(d, "\tкрасная")

for div in range(2, 485):
    if 485 % div == 0:
        print(div)