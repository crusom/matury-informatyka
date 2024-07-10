nums = []

with open("liczby_new.txt", "r") as f:
#with open("przyklad_new.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        nums.append(int(line))

print("4.1")
asdf = 0
asdf1 = None
for num in nums:
    if str(num)[0] == str(num)[len(str(num))-1]:
        if asdf1 == None:
            asdf1 = str(num)
        asdf += 1
print(asdf1, asdf)

print("4.2")

max_czynniki = 0
max_czynniki_num = 0

max_rozne = 0
max_rozne_num = 0

for num in nums:
    czynniki = []
    i = 2
    n = num
    while n % i == 0:
        czynniki.append(i)
        n //= i
    i += 1
    while n > 1:
        while n % i == 0:
            czynniki.append(i)
            n //= i
        i += 2

    if len(czynniki) > max_czynniki:
        max_czynniki = len(czynniki)
        max_czynniki_num = num
    if len(set(czynniki)) > max_rozne:
        max_rozne = len(set(czynniki))
        max_rozne_num = num
print(max_czynniki_num, max_czynniki)
print(max_rozne_num, max_rozne)

trojki = []
len_nums = len(nums)
nums = sorted(nums)
for index_1 in range(len_nums):
    n1 = nums[index_1]
    for index_2 in range(index_1+1, len_nums):
        n2 = nums[index_2]
        if n2 % n1 == 0 and n1 != n2:
            for index_3 in range(index_2+1, len_nums):
                n3 = nums[index_3]
                if n3 % n2 == 0 and n3 != n2:
                    trojki.append((n1, n2, n3))

piatki = []
#print(trojki)
for index_1 in range(len_nums):
    n1 = nums[index_1]
    for index_2 in range(index_1+1, len_nums):
        n2 = nums[index_2]
        if n2 % n1 == 0 and n1 != n2:
            for index_3 in range(index_2+1, len_nums):
                n3 = nums[index_3]
                if n3 % n2 == 0 and n3 != n2:
                    for index_4 in range(index_3+1, len_nums):
                        n4 = nums[index_4]
                        if n4 % n3 == 0 and n4 != n3:
                            for index_5 in range(index_4+1, len_nums):
                                n5 = nums[index_5]
                                if n5 % n4 == 0 and n5 != n4:
                                    piatki.append((n1,n2,n3,n4,n5))
print("4.3")
print(len(trojki))
print(len(piatki))
