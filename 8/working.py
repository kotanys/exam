from itertools import permutations

cnt = 0
for A in set(permutations("КАПКАН")):
    w = "".join(A)
    if w[0] == w[1] or w[1] == w[2] or w[2] == w[3] or w[3] == w[4] or w[4] == w[5]:
        continue
    cnt += 1
print(cnt)