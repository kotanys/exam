from functools import lru_cache

def moves(m: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    x, y = m
    return (x + y, y), (x, y + x)

@lru_cache
def game(m):
    if any(sum(x) >= 57 for x in moves(m)):
        return "W1"
    #elif any(game(x) == "W1" for x in moves(m)):
    #    return "Neud"
    elif all(game(x) == "W1" for x in moves(m)):
        return "L1"
    elif any(game(x) == "L1" for x in moves(m)):
        return "W2"
    elif all(game(x) == "W2" for x in moves(m)):
        return "L2"
    
for s in range(1, 47):
    if game((s, s)) == "L2":
        print(s)
    #if game((10, s)) == "Neud":
    #    print(s)