from math import ceil

above = []
under = []
with open("C:\\Users\\Пользователь\\Desktop\\Егэшные решения\\26.web_5.txt") as file:
    file.readline()
    for line in file:
        n = int(line)
        if n > 120:
            above.append(n)
        else:
            under.append(n)
above.sort()
mx = above[len(above) // 2 - 1]
for i in range(len(above) // 2):
    above[i] *= 0.75
sm = ceil(sum(under) + sum(above))
print(sm, mx)