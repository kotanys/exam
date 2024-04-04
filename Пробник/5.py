def r(n: int) -> int:
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b += '0'
        b = '10' + b[2:]
    else:
        b += '11'
        b = '11' + b[2:]
    return int(b, 2)

for n in range(200, 1, -1):
    if r(n) < 99:
        print(n, r(n+1))
        break