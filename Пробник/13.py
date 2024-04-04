import ipaddress
net = ipaddress.ip_network('192.168.48.160/255.255.255.240', False)
cnt = 0
for add in net:
    s = bin(int(add))[2:]
    if s.count('1') % 2 != 0:
        cnt += 1
print(cnt)