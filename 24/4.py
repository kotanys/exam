from itertools import product

f = open(".\\24\\4.txt")
l = f.readline()

def split(string, delimiter):
    return " ".join(string.split(delimiter))

for c in product("UMS", repeat=2):
    l = split(l, "".join(c))
print(max(map(len, l.split())))