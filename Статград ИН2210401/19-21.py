from functools import lru_cache


def moves(m: tuple[int, int]):
    mx, mn = max(m), min(m)
    out = [(mx+1, mn), (mx+2, mn), (mx+3,mn)]
    if mx != mn:
        out.append((mx, mn*2))
    return out

@lru_cache
def game(m: tuple[int, int]):
    if any(sum(x) >= 41 for x in moves(m)):
        return "W1"
    if all(game(x) == "W1" for x in moves(m)):
        return "L1"
    if any(game(x) == "L1" for x in moves(m)):
        return "W2"
    if all(game(x) in ("W2","W1") for x in moves(m)):
        return "L12"

def main():
    for s in range(1, 24):
        if game((17, s)) == "L12":
            print(s)

if __name__ == "__main__":
    main()
    
"""
19 -- 28
20 -- 2029
21 -- 9
"""