a = int(input())
x = int(input())
M = int(input())

adder = a
b = 1

while x != 0:
    if x & 1 == 1:
        b *= adder
    adder *= adder
    x = x >> 1

print(b % M)
