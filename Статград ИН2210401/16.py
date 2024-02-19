a_cache = [-1]*15
def F_iter(a, b):
    a = a % b
    a_in = a
    if a_cache[a_in] != -1:
        return a_cache[a_in]
    while b != 0:
        if a >= b > 0:
            a, b = a-b, b
        else:
            a, b = b, a
    a_cache[a_in] = a
    return a
cnt = 0
for n in range(123456795, 1234567889):
    if F_iter(n, 14) == 1:
        cnt += 1
print(cnt)