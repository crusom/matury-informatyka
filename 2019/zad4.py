def factorial(k):
    res = 1
    for i in range(k, 0, -1):
        res *= i
    return res

def nwd(a,b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

nums = []
with open("Dane_PR2/liczby.txt") as f:
    lines = f.readlines()
    for line in lines:
        nums.append(int(line.strip()))

powers_of_three = []
n = 1
while n <= 100000:
    powers_of_three.append(n)
    n *= 3

nums_pow_of_three = 0
for num in nums:
    if num in powers_of_three:
        nums_pow_of_three += 1

print("4.1")
print(nums_pow_of_three)

print("4.2")
for num in nums:
    sum_of_fact = 0
    for c in str(num):
        sum_of_fact += factorial(int(c))
    if sum_of_fact == num:
        print(num)

max_length = 0
max_factor = 0

for index, num in enumerate(nums):
    cur_length = 0
    cur_factor = num
    cur_nwd    = 0

    last_nwd = 0
    for e in nums[index:]:
        last_nwd = nwd(last_nwd, e)
        if last_nwd == 1:
            if cur_length > max_length:
                max_length = cur_length
                max_factor = cur_factor
                max_nwd    = cur_nwd
            cur_length = 1
        else:
            cur_nwd = last_nwd
            cur_length += 1

print("4.3")
print(max_factor, max_length, max_nwd)
