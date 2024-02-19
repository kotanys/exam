def win1(a, b):
    return ((a + 3) * b) >= 75 or (a * (b + 3)) >= 75 or ((a + 4) * b) >= 75 or (a * (b + 4)) >= 75

def loss1(a, b):
    return not win1(a, b) and win1(a + 3, b) and win1(a, b + 3) and win1(a + 4, b) and win1(a, b + 4)

def win2(a, b):
    return loss1(a + 3, b) or loss1(a, b + 3) or loss1(a + 4, b) or loss1(a, b + 4)

def loss12(a, b):
    return (win1(a + 3, b) or win2(a + 3, b)) and (win1(a + 4, b) or win2(a + 4, b)) and \
        (win1(a, b + 4) or win2(a, b + 4)) and (win1(a, b + 3) or win2(a, b + 3)) and \
            not (win1(a + 3, b) and win1(a, b + 3) and win1(a + 4, b) and win1(a, b + 4))

def main():
    x = 1
    for s in range(1, 74):
        if loss12(x, s):
            print(s)

if __name__ == "__main__":
    main()