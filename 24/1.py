f = open(".\\24\\1.txt")
l = f.readline()
l = l.split("Y")
a = []
for x in l:
    a.extend(x.split("Z"))
print(max(map(len, a)))
