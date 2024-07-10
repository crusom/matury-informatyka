#from math import abs

pixels = []
with open("Dane_PR2/dane.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        s = line.split()
        int_s = []
        for i in list(s):
            int_s.append(int(i))
        pixels.append(int_s)

print("6.1")
min_p = 1000;
max_p = 0;
for row in pixels:
    for pixel in row:
        pixel = int(pixel)
        if pixel > max_p:
            max_p = pixel
        if pixel < min_p:
            min_p = pixel
print("min: " + str(min_p),"max: " + str(max_p))

print("6.2")
delete = 0
for row in pixels:
    for i in range(len(row)):
        if row[i] != row[len(row) - 1 - i]:
            delete += 1
            break
print(delete)

print("6.3")
c = 0
for row_i, row in enumerate(pixels):
    for i in range(len(row)):
        if i != 0:
            if abs(row[i - 1] - row[i]) > 128:
                c += 1           
                continue 
        if row_i != 0:
            if abs(pixels[row_i - 1][i] - row[i]) > 128:
                c += 1
                continue
        if i != len(row)-1:
            if abs(row[i + 1] - row[i]) > 128:
                c += 1
                continue
        if row_i != len(pixels)-1:
            if abs(pixels[row_i + 1][i] - row[i]) > 128:
                c += 1
            continue
print(c)
print("6.4")
max_length = 0;
for x in range(len(pixels[0])):
    length = 1;
    prev_pixel = None
    for y in range(len(pixels)):
        try:
            if pixels[y][x] == prev_pixel:
                length += 1
            else:
                prev_pixel = pixels[y][x]
                if length > max_length:
                    max_length = length
                length = 1
        except Exception:
            pass
print(max_length)
