nums = []
with open("Dane_PR2/liczby.txt") as f:
    lines = f.readlines()
    for line in lines:
        nums.append(line.strip())

more_zeroes = 0
for num in nums:
    if num.count('0') > num.count('1'):
        more_zeroes += 1
print("zad 4.1")
print(more_zeroes)

division_2 = 0
division_8 = 0

for num in nums:
    if int(num, 2) % 2 == 0:
        division_2 += 1
    if int(num, 2) % 8 == 0:
        division_8 += 1

print("zad 4.2")
print(division_2, division_8)

max_num = 0
min_num = 0xfffffffff
min_line_n =  0
max_line_n =  0
for index, num in enumerate(nums):
    n_int = int(num, 2)
    if n_int > max_num:
        max_num = n_int
        max_line_n = index + 1

    if n_int < min_num:
        min_num = n_int
        min_line_n = index + 1
print("zad 4.3")
print(min_line_n, max_line_n)
