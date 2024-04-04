for x in list(range(1,10)) + list('ABCDEF'):
    s = int(str(x) + "ABC", 16) + int("DEF" + str(x), 16)
    if s % 15 == 0:
        print(x, s//15)