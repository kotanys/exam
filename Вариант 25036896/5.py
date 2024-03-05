def f(n):
    b = bin(n)[2:]
    if sum(map(int, b)) % 2 != 0:
        b = b + "11"
    else:
        b = "11" + b
    return int(b, 2)

for i in range(50):
    print(i, f(i))