A = []
B = []
with open("26.txt") as file:
    _, budget, A_count = file.readline().split()
    budget = int(budget)
    A_count = int(A_count)
    for line in file:
        n, tp = line.split()
        n = int(n)
        if tp == 'A':
            A.append(n)
        else:
            B.append(n)
A.sort()
B.sort()

A_bought = []
B_bought = []
for i in range(A_count):
    A_bought.append(A[i])
    budget -= A[i]

for b in B:
    if budget - b >= 0:
        B_bought.append(b)
        budget -= b
    else:
        break
def get_max_Btype(more_budget):
    for i in reversed(range(len(B_bought))):
        for k in range(i + 1, len(B)):
            if more_budget + B_bought[i] - B[k] >= 0:
                more_budget = more_budget + B_bought[i] - B[k]
                B_bought[i] = B[k]
                assert more_budget >= 0
            else:
                break
def get_discount():
    ds = 0
    combined = []
    combined.extend(A_bought)
    combined.extend(B_bought)
    combined.sort()
    for i in range(len(combined) // 4):
        ds += combined[i] * 0.33
    return ds
get_max_Btype(budget)
discount = get_discount()
budget += discount
get_max_Btype(budget)

print(sum(B_bought), round(discount))