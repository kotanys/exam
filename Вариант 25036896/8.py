from itertools import product
i = 1
for p in product("ГЕКЭ023", repeat=4):
    print(i, "".join(p))
    i += 1