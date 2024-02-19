with open("27B.txt") as file:
    file.readline()
    A = [int(x) for x in file.readlines()]
"""mxsm = -1
mxns = -1, -1
for i in range(len(A) - 1):
    for j in range(i + 1, len(A)):
        if abs(A[i] - A[j]) % 2 == 0 and (A[i] % 17 == 0 or A[j] % 17 == 0):
            if A[i] + A[j] > mxsm:
                mxsm = A[i] + A[j]
                mxns = A[i], A[j]
print(mxns)"""

evens, odds = [], []
for x in A:
    if x % 2 == 0:
        evens.append(x)
    else:
        odds.append(x)
evens.sort(reverse=True)
odds.sort(reverse=True)
ediv17 = None
emax = None
for e in evens:
    if ediv17 is not None and emax is not None:
        break
    if ediv17 is None and e % 17 == 0:
        ediv17 = e
    elif emax is None:
        emax = e
if ediv17 is None:
    ediv17 = -100000000000
odiv17 = None
omax = None
for o in odds:
    if odiv17 is not None and omax is not None:
        break
    if odiv17 is None and o % 17 == 0:
        odiv17 = o
    elif omax is None:
        omax = o
if odiv17 is None:
    odiv17 = -100000000000

if ediv17 + emax > omax + odiv17:
    print(ediv17, emax)
else:
    print(odiv17, omax)