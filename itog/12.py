def f(a, b):
    if a == b:
        return 1
    elif a < b:
        return 0
    else:
        return f(a - 1, b) + f(a//2, b) + f(a//3, b)
    
print(f(20, 9) * f(9, 1))