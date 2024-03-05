import ipaddress as ip
net = ip.ip_network("102.12.21.201/255.255.252.0", False)
ones_in_mask = "".join(map(lambda x: bin(int(x))[2:], "255.255.252.0".split("."))).count('1')

cnt = 0
for address in net:
    binadd = ".".join(map(lambda x: bin(int(x))[2:], str(address).split(".")))
    if (binadd.count("1") - ones_in_mask) % 2 == 0:
        cnt += 1
print(cnt)