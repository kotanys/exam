with open("24.txt") as f:
    data = f.readlines()

Alph = "QWERTYUIOPASDFGHJKLZXCVBNM"
mx = 0
mxstring = 0
for l in data:
    l = l.strip()
    mxstrings = dict.fromkeys(Alph, 0)
    letters = dict.fromkeys(Alph, 0)
    curstringlen = 1
    mxstrings[l[0]] = letters[l[0]] = 1
    for i in range(1, len(l)):
        letters[l[i]] += 1
        if l[i] == l[i - 1]:
            curstringlen += 1
        else:
            curstringlen = 1
        mxstrings[l[i]] = max(mxstrings[l[i]], curstringlen)
    
    for letter in mxstrings.keys():
        if mxstring <= mxstrings[letter]:
            mxstring = mxstrings[letter]
            mx = max(mx, letters[letter])
print(mx)