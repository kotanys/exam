from math import ceil, sqrt


with open("17a.txt") as f:
    a = [int(s) for s in f]

# возвращает количество семизначных чисел в списке
def cnt7d(l) -> int:
    lcnt = 0
    for x in l:
        if 1000000 <= x <= 9999999:
            lcnt += 1
    return lcnt

# решето Эратосфена
# возвращает список всех простых чисел вплоть до up_to
def get_primes(up_to: int) -> set[int]:
    is_prime = [True] * (up_to+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, ceil(sqrt(up_to + 1))):
        if is_prime[i] == False:
            continue
        for j in range(i*2, up_to + 1, i):
            is_prime[j] = False
    
    primes: list[int] = []
    for i in range(up_to + 1):
        if is_prime[i]:
            primes.append(i)
    return set(primes)
PRIMES = get_primes(10_000_000)

# возвращает список простых чисел в списке
def primes_in(l) -> list[int]:
    result = []
    for x in l:
        if x in PRIMES:
            result.append(x)
    return result

# возвращает количество чётных чисел в списке
def cnt_even(l) -> int:
    lcnt = 0
    for x in l:
        if x % 2 == 0:
            lcnt += 1
    return lcnt

max_prime = max(primes_in(a))
cnt = 0
max_product = 0
for i in range(len(a) - 4):
    cut = a[i:i+5]
    cond1 = cnt7d(cut) >= 1 # есть ли семизначное?
    cond2 = len(primes_in(cut)) > cnt_even(cut) # больше ли простых, чем чётных?
    cond3 = (max(cut) - min(cut)) < max_prime # разница меньше ли, чем наибольшее простое?
    if cond1 and cond2 and cond3:
        cnt += 1
        product = cut[0] * cut[1] * cut[2] * cut[3] * cut[4]
        max_product = max(max_product, product)
        
print(cnt, max_product)