data = [1, 2, 2, 4, 3, 3, 3, 2, 1, 5, 5, 3, 4, 4, 5]

subs = [[data[0]]]
rising = True
for i in range(1, len(data)):
    last = subs[-1][-1]
    if data[i] > last and rising:
        subs[-1].append(data[i])
    elif data[i] > last and not rising:
        subs.append([data[i]])
        rising = True
    elif data[i] < last:
        subs[-1].append(data[i])
        rising = False
    elif data[i] == last:
        subs.append([data[i]])

def get_cnt_subs(x: list):
    return (1 + len(x))*len(x) // 2
print(subs)
print(sum(map(get_cnt_subs, subs)))