def f(x: str):
    while "111" in x or "333" in x:
        if "111" in x:
            x = x.replace("111", "3", 1)
        else:
            x = x.replace("333", "1", 1)
    return x

a = []
for i in range(101, 200):
    s = "3"*i
    a.append((i, f(s)))

print(*a, sep="\n")