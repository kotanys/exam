# 1_000_000_000_000 = 10**12
def good(n):
    s = str(n)
    return s[:3] == "123" and s[4] == "4" and s[-4:] == "5679"

a = []
for i in range(123046606, 123945679, 4013):
    if good(i) and i % 4013 == 0:
        a.append((i, i // 4013))
for i in range(1230405865, 1239495679, 4013):
    if good(i) and i % 4013 == 0:
        a.append((i, i // 4013))
for i in range(12304006481, 12394995679, 4013):
    if good(i) and i % 4013 == 0:
        a.append((i, i // 4013))
for i in range(123040008628, 123949995679, 4013):
    if good(i) and i % 4013 == 0:
        a.append((i, i // 4013))
print(*a, sep="\n")