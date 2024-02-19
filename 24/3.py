f = open(".\\24\\3.txt")
l = f.readline()
l = l.replace("I", "E").replace("O", "E").replace("K", "M")
totalmax = 0
curmax = 0
for i in range(0, len(l) - 1, 2):
    if l[i] == "M" and l[i + 1] == "E":
        curmax += 1
        totalmax = max(totalmax, curmax)
    else:
        curmax = 0
curmax = 0
for i in range(1, len(l) - 1, 2):
    if l[i] == "M" and l[i + 1] == "E":
        curmax += 1
        totalmax = max(totalmax, curmax)
    else:
        curmax = 0
print(totalmax)