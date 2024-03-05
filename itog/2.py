s = "6"*70 + "7"*70 + "8"*70
while "67" in s or "87" in s or "86" in s:
    if "67" in s:
        s = s.replace("67", "76", 1)
    if "87" in s:
        s = s.replace("87", "78", 1)
    if "86" in s:
        s = s.replace("86", "68", 1)
print(s[4], s[112], s[32], sep="")