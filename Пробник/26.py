f = open('Пробник/26.txt')
n, m = map(int, f.readline().split())
a = list(map(int, f.readlines()))

mchecks = []
a.sort(reverse=True)
for i in range(m):
    mchecks.append(a[i])
S1 = sum(mchecks)
print(S1)
unique = sorted(set(mchecks))
S2 = S1
for i in range(len(unique)):
    if S2 - unique[i] > S1 * 0.75:
        S2 -= unique[i]
    else:
        break
print(S1, S2)