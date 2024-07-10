from collections import Counter

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    k = 3
    while k * k <= n:
        if n % k == 0:
            return False
        k += 2
    return True

nums = []

with open("DANE/liczby.txt") as f:
    lines = f.readlines()
    for line in lines:
        nums.append(int(line.strip()))

print("zad 4.1")
for num in nums:
    rev = int(str(num)[::-1])
    if rev % 17 == 0:
        print(rev)

max_rev = 0
max_org = 0
for num in nums:
    rev = int(str(num)[::-1])
    if abs(num-rev) > max_rev:
        max_rev = abs(num-rev)
        max_org = num
print("zad 4.2")
print(max_org, max_rev)
print("zad 4.3")
for num in nums:
    rev = int(str(num)[::-1])
    if is_prime(num) and is_prime(rev):
        print(num)

print("zad 4.3a")
c = Counter(nums)
print(len(sorted(c)))
print("zad 4.3b")
two_times = 0
for i in list(c.items()):
    if i[1] == 2:
        two_times += 1
print(two_times)
print("zad 4.3c")

three_times = 0
for i in list(c.items()):
    if i[1] == 3:
        three_times += 1
print(three_times)
