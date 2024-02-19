PATH = "C:\\Users\\Пользователь\\Desktop\\Егэшные решения\\Статград ИН2210401\\files\\09.csv"

data:list[list[int]] = []
with open(PATH) as file:
    for line in file:
        tpl = map(int, line.split(','))
        data.append(list(tpl))

counts = [0] * 1001
for line in data:
    for x in line:
        counts[x] += 1
good_count = 0
for line in data:
    good = False
    for x in line:
        x_count = 0
        for i in line:
            if i == x:
                x_count += 1
        if x_count == 1 and counts[x] - 1 == 45:
            good = True
            break
    if good:
        good_count += 1
        
        
print(good_count)