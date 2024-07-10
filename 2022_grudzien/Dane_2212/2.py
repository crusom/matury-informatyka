N = 100000

def strzalka(d, x_up, x_down):
    d[x_down] = x_up

def rysuj(d, x):
    if 2 * x <= N:
        strzalka(d, x, 2 * x)
        rysuj(d, 2 * x)
    if 2 * x + 1 <= N:
        strzalka(d, x, 2 * x + 1)
        rysuj(d, 2 * x + 1)
        
pary = []
with open("pary.txt") as f:
    lines = f.readlines()
    for line in lines:
        pary.append((int(line.strip().split()[0]), int(line.strip().split()[1])))

d = dict()
rysuj(d, 1)
for para in pary:
    a = para[1]
    found = False
    while a != 1:
        a = d[a]
        if a == para[0]:
            found = True
            break
    if found:
        print(para)
