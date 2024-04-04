good = []
if 12345 % 46 == 0: # 12345
    good.append(12345)
for s in range(1234500, 1234599+1): # 12345..
    if s % 46 == 0:
        good.append(s)
for s in range(1203450, 1293459+1): # 12.345.
    if str(s)[:2] == '12' and str(s)[3:6] == '345' and s % 46 == 0:
        good.append(s)
for s in range(1200, 1299+1): # 12..345
    s0 = int(str(s) + '345')
    if s0 % 46 == 0:
        good.append(s0)
for s in range(123450, 123459+1): # 12345.
    if s % 46 == 0:
        good.append(s)
for s in range(120345, 129345+1, 1000): # 12.345:
    if s % 46 == 0:
        good.append(s)
print(*[f"{n} {n//46}" for n in good], sep='\n')