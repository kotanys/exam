with open("24.3.5_Gkd1VXk.txt") as file:
    a = file.readline().strip()

b = dict.fromkeys("QWERTYUIOPASDFGHJKLZXCVBNM", 0)
for i in range(1, len(a) - 1):
    if a[i - 1] != 'D' or a[i + 1] != 'P':
        continue
    b[a[i]] += 1
    
mx = 0
maxes = []
for k, v in b.items():
    if v > mx:
        maxes = [(k, v)]
        mx = v
    elif v == mx:
        maxes.append((k, v))
print(maxes)