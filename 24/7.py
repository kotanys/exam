f = open(".\\24\\7.txt")
mx = -1
for l in f:
    if len([c for c in l if c.isupper()]) < 40:
        continue
    for c in "qwertyuiopasdfghjklzxcvbnm":
        mx = max(mx, l.rfind(c) - l.find(c))
print(mx)