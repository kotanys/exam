f = open('Пробник/24.txt')
a = f.readlines()
mx = 0
for i,line in enumerate(a):
    letter_count = {}
    for c in line:
        letter_count.setdefault(c, 0)
        letter_count[c] += 1
    for letter in [c for c in letter_count.keys() if letter_count[c] >= 2]:
        between = max(map(len, line.split(letter)))
        mx = max(mx, between)
print(mx)