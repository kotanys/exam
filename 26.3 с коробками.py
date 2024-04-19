a = [], []  # [0] R, [1] B 
def get_input(a):
    with open("26.3.txt") as f:
        for l in f:
            split = l.split()
            n, color = int(split[0]), (1 if split[1] == 'B' else 0)
            a[color].append(n)

get_input(a)

a[0].sort(reverse=True)
a[1].sort(reverse=True)


blocks = []
while a[0] and a[1]:
    cc = 0 if a[0][0] > a[1][0] else 1
    current = [a[cc][0]]
    del a[cc][0]
    cc = 1 if cc == 0 else 0
    i = [0, 0]
    while i[cc] < len(a[cc]):
        if a[cc][i[cc]] <= current[-1] - 8:
            current.append(a[cc][i[cc]])
            del a[cc][i[cc]]
            cc = 1 if cc == 0 else 0
        else:
            i[cc] += 1
    blocks.append(current)
for r in a[0]:
    blocks.append([r])
for b in a[1]:
    blocks.append([b])
print(len(blocks), max(map(len, blocks)))