def W1(a, b) -> bool:
    return (a - 1 + b <= 40) or (a // 2 + b <= 40) or (b // 2 + a <= 40)

def L1(a, b) -> bool:
    return not W1(a, b) and W1(a - 1, b) and W1(a, b - 1) and W1(a // 2, b) and W1(a, b // 2)

def W2(a, b) -> bool:
    return not L1(a, b) and (L1(a - 1, b) or L1(a, b - 1) or L1(a // 2, b) or L1(a, b // 2))

def L12(a, b) -> bool:
    return ((W1(a - 1, b) or W2(a - 1, b)) and (W1(a, b - 1) or W2(a, b - 1)) and (W1(a // 2, b) or W2(a // 2, b)) and (W1(a, b // 2) or W2(a, b // 2))) \
        and not (W1(a - 1, b) and W1(a, b - 1) and W1(a // 2, b) and W1(a, b // 2))

for N in range(1000, 34, -1):
    if W1(5, N) or W1(6, N - 1) or W1(3, N) or W1(6, N//2):
        print("19:", N)
        break
print()
for N in range(1000, 34, -1):
    if not W1(6, N) and W2(6, N):
        print("20:", N)
print()
for N in range(1000, 34, -1):
    if L12(6, N):
        print(N)