for i in range(95, 120):
    s = '0'*i
    while '000' in s:
        s=s.replace('000', '8', 1)
        s=s.replace('8888','00', 1)
    if s == '00':
        print(i)