print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = (w or x or not z or y) and (w or x or not z or not y) and (w or not x or not z or not y)
                if not F:
                    print(x, y, w, z)