s = 5**2004 - 5**1016 - 25**508 - 5**400 + 25**250 - 27
a = []
while s != 0:
    a.append(s % 5)
    s //= 5
print(a.count(4))