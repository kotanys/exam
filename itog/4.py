def readfile(fname: str) -> tuple[int, list[int]]:
    with open(fname) as f:
        n = int(f.readline())
        a = map(int, f.readlines())
    return n, list(a)

def perebor(fname: str) -> int:
    n, a = readfile(fname)
    mn = 10**10
    best_i = -1
    for i in range(n):
        current = 0
        for j in range(n):
            dist = min(abs(i - j), n - abs(i - j))
            current += dist * a[j]
        if mn > current:
            mn = current
            best_i = i
    return best_i + 1

"""def fast(fname: str) -> int:
    n, a = readfile(fname)"""
    

print("t =", perebor("itog/27.t.txt"))
print("A =", perebor("itog/27.A.txt"))