f = open("Вариант\\24.txt")
s = f.readline()
f.close()

current = 1 if s[0] != s[1] else 0
mx = current
biggest_rn = True
for i in range(1, len(s) - 1):
    if s[i - 1] != s[i] and s[i] != s[i + 1]:
        current += 1
    else:
        current = 0
    if current > mx:
        mx = current
        biggest_rn = True
    else:
        biggest_rn = False

if biggest_rn and s[-2] != s[-1]:
    mx += 1
print(mx)