with open("усл3.txt") as file:
    a = file.readline().strip()

b = dict.fromkeys("QWERTYUIOPASDFGHJKLZXCVBNM", 0)
for i in range(len(a) - 3):
    cut = a[i:i+4]
    if not (cut[0] == cut[1] == cut[2]):
        continue
    b[cut[3]] += 1

mx = 0
ltrs = []
for k, v in b.items():
    if v > mx:
        ltrs = [(k, v)]
        mx = v
    elif v == mx:
        ltrs.append((k, v))
print(ltrs)