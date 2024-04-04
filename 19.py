def win1(a: int, b: int):
    return (a - 1 + b) <= 20 or (a //2 + b) <= 20 or (a + b // 2) <= 20

def loss1(a, b):
    return not win1(a, b) and win1(a - 1, b) and win1(a, b - 1) and win1(a // 2, b) and win1(a, b // 2)

def win2(a, b):
    return loss1(a - 1, b) or loss1(a, b - 1) or loss1(a // 2, b) or loss1(a, b // 2)

def loss12(a, b):
    return (win1(a - 1, b) or win2(a-1, b)) and (win1(a, b - 1) or win2(a, b - 1)) \
        and (win1(a // 2, b) or win2(a//2, b)) and (win1(a, b//2) or win2(a, b//2))\
        and not (win1(a- 1, b) and win1(a, b - 1) and win1(a//2, b) and win1(a, b // 2))

print("--19--")
for S in reversed(range(11, 200)):
    if win1(10 - 1, S) or win1(10, S - 1) or win1(10 // 2, S) or win1(10, S//2):
        print(S)
        break
    
print("--20--")
for S in range(11, 200):
    if win2(10, S):
        print(S, end="")
print()

print("--21--")
for S in reversed(range(11, 200)):
    if loss12(10, S):
        print(S)
        break