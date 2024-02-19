import re

f = open(".\\24\\5.txt")
l = f.readline()
n = 1
while re.search("(AXO|XAO){" + str(n) + "}", l):
    print(n)
    n += 1