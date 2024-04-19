with open("24.txt") as f:
    a = f.readline()
    
E = 'E'
S = 'S'

betw = a.split(E)[1:-1]
longest = 0
for i in range(len(betw)):
    cur = 1
    for j in range(i, len(betw)):
        if betw[j].count(S) <= 3:
            cur += len(betw[j]) + 1
        else:
            break
    longest = max(cur, longest)
print(longest)