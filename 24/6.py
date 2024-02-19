import re

f = open(".\\24\\6.txt")
l = f.readline()
n = 1
while re.search("(AN|NT){" + str(n) + "}", l):
    print(n)
    n += 1