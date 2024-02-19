goods = []
with open("26.web_1.txt") as file:
    capacity, _ = file.readline().split()
    capacity = int(capacity)
    for line in file:
        goods.append(int(line))
goods.sort()
weight = 0
cnt = 0
for x in goods:
    if weight + x <= capacity:
        weight += x
        cnt += 1
        last = x
    elif weight - last + x <= capacity:
        weight = weight - last + x
        last = x
    else:
        break
print(cnt, last)