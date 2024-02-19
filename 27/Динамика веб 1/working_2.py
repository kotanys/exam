f = open("27_B.txt")
n = int(f.readline())
mins = [1000000001] * 43
minl = [0] * 43
sm = 0
maxsum = 0
minlen = 0
for i in range(1, n + 1):
    sm += int(f.readline())
    d = sm % 43
    if d == 0:
        maxsum = sm
        minlen = i
    else:
        ms = sm - mins[d]
        l = i - minl[d]
        if ms > maxsum:
            maxsum = ms
            minlen = l
        if (ms == maxsum) and (l < minlen):
            maxsum = ms
            minlen = l
        if sm < mins[d]:
            mins[d] = sm
            minl[d] = i
print(minlen)