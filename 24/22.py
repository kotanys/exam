f = open(".\\24\\22.txt")
mx = -1
mxl = ''
for l in f:
    if l.count("a") >= 20:
        continue
    for c in "qwertyuiopasdfghjklzxcvbnm":
        if l.rfind(c) - l.find(c) - 1 > mx:
            mxl = c
        mx = max(mx, l.rfind(c) - l.find(c) - 1)
print(mx, mxl)