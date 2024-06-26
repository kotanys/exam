from math import tan, radians, sqrt

# Повтори 123 [Вперед 101 Направо 120].
# Определите, сколько точек с целочисленными координатами будут находится внутри области, ограниченной линией,
# заданной данным алгоритмом. Точки на линии учитывать не следует.

#! ФОРМУЛА ПИКА
#! S = В + Г/2 - 1, где В - точки внутри, Г - точки на границе
cnt = 0
for x in range(100):
    for y in range(150):
        if 0 < x < sqrt(101*101 - 101*101/4) \
           and x*tan(radians(30)) < y < 101 - x*tan(radians(30)):
            print(x, y)
print(cnt)