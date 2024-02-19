goods = []
with open("26.web_2.txt") as file:
    capacity, _ = file.readline().split()
    capacity = int(capacity)
    for line in file:
        goods.append(int(line))
goods.sort()
weight = 0
cnt = 0
cant_carry = len(goods)
for x in goods:
    if weight + x <= capacity:
        weight += x
        cnt += 1
        last = x
        cant_carry -= 1
    elif weight - last + x <= capacity:
        weight = weight - last + x
        last = x
        cant_carry -= 1
    else:
        break
print(cnt, cant_carry)