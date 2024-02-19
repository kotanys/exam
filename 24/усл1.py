with open("усл1.txt") as f:
    lines = f.readlines()
    
a = []
for line in lines:
    line = line.strip()
    b = dict.fromkeys("QWERTYUIOPASDFGHJKLZXCVBNM", 0)
    for i in range(1, len(line)):
        if line[i - 1] == 'B':
            b[line[i]] += 1
    mx = 0
    current_max = []
    for k, v in b.items():
        if v > mx:
            current_max = [k]
            mx = v
        elif v == mx:
            current_max.append(k)
    a.extend(current_max)
b = dict.fromkeys("QWERTYUIOPASDFGHJKLZXCVBNM", 0)
for c in a:
    b[c] += 1
print(max(b.values()))