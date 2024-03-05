def r(n):
    s = bin(n)[2:]
    s += s[-1]
    if bin(n).count("1") % 2 == 0:
        s += "0"
    else:
        s += "1"
    if s.count("1") % 2 == 0:
        s += "0"
    else:
        s += "1"
    return int(s, 2)
        
for N in range(100):
    if r(N) > 92:
        print(r(N))
        break