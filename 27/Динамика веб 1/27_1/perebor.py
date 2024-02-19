from math import ceil, sqrt
def is_prime(x):
    for div in range(2, ceil(sqrt(x))):
        if x % div == 0:
            return False
    return x >= 2

file = open("27/Динамика веб 1/27_1_A.txt")
file.readline()

data = [int(s) for s in file]
prime_data = [is_prime(x) for x in data]
max_sum = -1
for i in range(len(data)):
    for j in range(i, len(data)):
        if sum(prime_data[i:j+1]) % 7 == 0:
            max_sum = max(max_sum, sum(data[i:j+1]))
print(max_sum)