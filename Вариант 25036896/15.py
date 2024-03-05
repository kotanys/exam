from itertools import count

def f(x, y, A):
    return ((2*x + 3*y) != 150) or (x < A) and (y < A)

for A in count(1):
    good = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not f(x, y, A):
                good = False
                break
        if not good:
            break
    if good:
        print(A)
        break