def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def calc(a, x, m):
    adder = a
    b = 1

    while x != 0:
        if x & 1 == 1:
             b *= adder
        adder *= adder
        x = x >> 1
    return b % m

def nwd(a,b):
    if b == 0:
        return a

    return nwd(b, a%b)

liczby = []
with open("Dane_2203/liczby.txt") as f:
    lines = f.readlines()
    for line in lines:
        liczby.append([int(x) for x in line.split()])

primes_len = 0
for liczb in liczby:
    if is_prime(liczb[0]):
        primes_len += 1
print(primes_len)

ile_wzglednie_pierwsze = 0
for liczb in liczby:
    M = liczb[0]
    a = liczb[1]
    if nwd(a,M) == 1:
        ile_wzglednie_pierwsze += 1
print(ile_wzglednie_pierwsze)

nasze_x = 0
for liczb in liczby:
    M = liczb[0]
    a = liczb[1]
    b = liczb[2]
    adder = a
    for i in range(M):
        #print(a, x, M, calc(a,x,M), b)
        if adder % M == b:
            nasze_x += 1
            break
        adder *= a

print(nasze_x)
