import sys

sys.setrecursionlimit(10000)

def F(n):

    if n == 1: 

        return 1 

    else:
        return 2 * n * F(n - 1) - 1

print(F(2000) / F(1997))