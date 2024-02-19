from functools import lru_cache

def moves(m):
    a, b = m
    return [(a + 2, b), (a, b + 2), (a*2, b), (a, b*2)]

@lru_cache
def game(m):
    if any(sum(x) >= 65 for x in moves(m)):
        return "W1"
    if all(game(x) == "W1" for x in moves(m)):
        return "L1"
    if any(game(x) == "L1" for x in moves(m)):
        return "W2"
    if all(game(x) in ["W2", "W1"] for x in moves(m)):
        return "L12"
    
for s in range(1, 62):
    if game((3, s)) == "L12":
        print(s, end=" ")