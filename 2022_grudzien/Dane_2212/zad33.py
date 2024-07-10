from math import sqrt
nums = []
with open("liczby.txt") as f:
    lines = f.readlines()
    for line in lines:
        nums.append(int(line.strip()))

max_n = max(nums)
primes = [True] * (max_n)
primes[0] = False
primes[1] = False

for i in range(2, int(sqrt(max_n))):
    if primes[i] == True:
        for j in range(i*i, max_n, i):
            primes[j] = False

only_primes = []
for index, prime in enumerate(primes):
    if prime == True:
        only_primes.append(index)

max_k = 0
min_k = 9999999999
look_max_n = 0
look_min_n = 0
for num in nums:
    k = 0
    for p in only_primes:
        if p > num // 2:
            break
        if primes[num - p]:
            k += 1
    if k > max_k:
        max_k = k
        look_max_n = num
    if k < min_k:
        min_k = k
        look_min_n = num
print("zad 3.3")
print(look_max_n, max_k)
print(look_min_n, min_k)
print("zad 3.4")

h = dict()
for num in nums:
    for c in str(hex(num))[2:]:
        if not c in h:
            h[c] = 1
        else:
            h[c] += 1

for i in sorted(h.items()):
    print(i)
