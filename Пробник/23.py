def f(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    sm = f(s+2, e)
    if s % 2 == 0:
        sm += f(s*2+1, e)
    else:
        sm += f(s*2, e)
    return sm

print(f(2, 90))