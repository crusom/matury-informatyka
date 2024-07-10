nums = []
words = []

with open("Dane_PR2/pary.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        nums.append(int(line.split()[0]))
        words.append(line.split()[1])

n = 100
primes_list = [True] * n

# 1, _2_, 3, 4, 5, 6, 7, 8, 9, 10
# 1, 2, _3_, x4x, 5, x6x, 7, x8x, 9, x10x
# 1, 2, 3, x_4_x, 5, x6x, 7, x8x, x9x, x10x
# 1, 2, 3, x4x, x_5_x, x6x, 7, x8x, x9x, x10x

for i in range(2, 11):
    if primes_list[i] == True:
        for j in range(2, n):
            if j * i < n:
                primes_list[j * i] = False
            else:
                break

print("zad 4.1")
for num in nums:
    if num % 2 != 0:
        continue
    for index, prime in enumerate(primes_list):
        if index < 3:
            continue
        if prime and primes_list[num - index]:
            print(num, index, num - index)
            break

print("zad 4.2")
for word in words:
    cur_c = 0
    cur_max = 0
    final_max = 0
    final_c = 0
    for c in word:
        if c != cur_c:
            cur_c = c
            cur_max = 1
        else:
            cur_max += 1

        if cur_max > final_max:
            final_max = cur_max
            final_c = cur_c

    print(str(final_c) * final_max, final_max)

d = {}
for i in range(len(words)):
    if len(words[i]) == nums[i]:
        n = nums[i]
        w = words[i]
        if n not in d.keys():
            d[n] = [w]
        else:
            d[n].append(w)

min_n = min(d.keys())

word_min = "z" * 1000 
for word in d[min_n]:
    if word < word_min:
        word_min = word

print("zad 4.3")
print(min_n, word_min)
