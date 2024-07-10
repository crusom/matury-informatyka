import math
r = 200
a = 200
b = 200
cords = []
with open("Dane_PR2/punkty.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        s = line.split()
        s_int = []
        for i in s:
            s_int.append(int(i))
        cords.append(s_int)

print("4.1")
brzeg_suma = 0
wnetrze_suma = 0
for cord in cords:
    x = cord[0]
    y = cord[1]

    if (x-a)**2 + (y-b)**2 == r**2:
        print(x, y)
    elif (x-a)**2 + (y-b)**2 < r**2:
        wnetrze_suma += 1

print(wnetrze_suma)
print("4.2")
kwad = 0
kolo = 0
for i in range(len(cords)):
    x = cords[i][0]
    y = cords[i][1]
    kwad += 1
    if (x-a)**2 + (y-b)**2 <= r**2:
        kolo += 1
    if i == 1000-1:
        print((kolo*(400**2)) / (kwad*(r**2)))
    if i == 5000-1:
        print((kolo*(400**2)) / (kwad*(r**2)))
print((kolo*(400**2)) / (kwad*(r**2)))

print("4.3 dane")
kwad = 0
kolo = 0
for i in range(1700):
    x = cords[i][0]
    y = cords[i][1]
    kwad += 1
    if (x-a)**2 + (y-b)**2 <= r**2:
        kolo += 1
    moje_pi = (kolo*(400**2)) / (kwad*(r**2))
    print(str(1+i) + "\t" + str(abs(math.pi-moje_pi))[:6])
