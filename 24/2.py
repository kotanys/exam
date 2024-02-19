f = open(".\\24\\2.txt")
l = f.readline()
a = l.split("C")
mx = -1
for i in range(len(a) - 1):
    mx = max(mx, len(a[i]) + len(a[i+1]) + 1)
print(mx)