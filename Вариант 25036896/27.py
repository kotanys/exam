def tuple_cast(s: str) -> tuple[int, int]:
    split = s.split()
    return (int(split[0]), int(split[1]))

def f(fname: str) -> int:
    with open(fname) as f:
        f.readline()
        a = list(map(tuple_cast, f.readlines()))

    odd_cnt = 0
    sm = 0
    for t in a:
        mx_t = max(t)
        sm += mx_t
        if mx_t % 2 != 0:
            odd_cnt += 1

    if odd_cnt % 2 == 0:
        return sm

    diff = [abs(x[0] - x[1]) for x in a if x[0] % 2 != x[1] % 2]
    return sm - min(diff)

print(f("Вариант 25036896/27A.txt"))
print(f("Вариант 25036896/27B.txt"))