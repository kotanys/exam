from ipaddress import ip_network

mxsum = -1
for A in reversed(range(256)):
    for B in reversed(range(256)):
        if A + B < mxsum:
            continue
        net = ip_network(f"196.{A}.{B}.52/255.255.255.248", False)
        for address in net:
            bin_repr = bin(int(address))[2:]
            l, r = bin_repr[:-16], bin_repr[-16:]
            if l.count("0") <= r.count("1"):
                break
        else:
            mxsum = A + B
print(mxsum)