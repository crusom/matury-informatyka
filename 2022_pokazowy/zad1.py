plansze = []
plansze.append([])

with open("Dane_2203/szachy.txt") as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        if line[0] == '\n':
            i += 1
            plansze.append([])
            continue
        plansze[i].append(line.strip())

przynajmniej_jedna = 0
max_kolumn = 0
for p in plansze:
    ile_kolumn = 0
    for y in range(8):
        puste = True
        for x in range(8):
            if p[x][y] != '.':
                puste = False
                break
        if puste:
            ile_kolumn += 1

    if ile_kolumn != 0:
        przynajmniej_jedna += 1
    if ile_kolumn > max_kolumn:
        max_kolumn = ile_kolumn

print(przynajmniej_jedna, max_kolumn)

piony = ['k', 'w', 's', 'h', 'g', 'p']

min_rown = 0xfffffffff
ile_rown = 0
for p in plansze:
    d = dict()
    d['.'] = 0
    for pion in piony:
        d[pion] = 0
        d[pion.upper()] = 0
    for y in range(8):
        for x in range(8):
            d[p[x][y]] += 1
    czy_rownowaga = True
    ile = 0
    for pion in piony:
        ile += d[pion] + d[pion.upper()]
        if d[pion] != d[pion.upper()]:
            czy_rownowaga = False
            break
    if czy_rownowaga:
        ile_rown += 1
        if ile < min_rown:
            min_rown = ile
print(ile_rown, min_rown)

biale_rachuje_czarne = 0
for p in plansze:
    found = False
    for y in range(8):
        for x in range(8):
            if p[x][y] == 'k':
                for k_y in range(y + 1, 8):
                    if p[x][k_y] != '.' and p[x][k_y] != 'W':
                        break
                    if p[x][k_y] == 'W':
                        found = True
                        break
                for k_y in range(y - 1, -1, -1):
                    if p[x][k_y] != '.' and p[x][k_y] != 'W':
                        break
                    if p[x][k_y] == 'W':
                        found = True
                        break
                for k_x in range(x + 1, 8):
                    if p[k_x][y] != '.' and p[k_x][y] != 'W':
                        break
                    if p[k_x][y] == 'W':
                        found = True
                        break
                for k_x in range(x - 1, -1, -1):
                    if p[k_x][y] != '.' and p[k_x][y] != 'W':
                        break
                    if p[k_x][y] == 'W':
                        found = True
                        break

    if found:
        biale_rachuje_czarne += 1

czarne_rachuje_biale = 0
for p in plansze:
    found = False
    for y in range(8):
        for x in range(8):
            if p[x][y] == 'K':
                for k_y in range(y + 1, 8):
                    if p[x][k_y] != '.' and p[x][k_y] != 'w':
                        break
                    if p[x][k_y] == 'w':
                        found = True
                        break
                for k_y in range(y - 1, -1, -1):
                    if p[x][k_y] != '.' and p[x][k_y] != 'w':
                        break
                    if p[x][k_y] == 'w':
                        found = True
                        break
                for k_x in range(x + 1, 8):
                    if p[k_x][y] != '.' and p[k_x][y] != 'w':
                        break
                    if p[k_x][y] == 'w':
                        found = True
                        break
                for k_x in range(x - 1, -1, -1):
                    if p[k_x][y] != '.' and p[k_x][y] != 'w':
                        break
                    if p[k_x][y] == 'w':
                        found = True
                        break

    if found:
        czarne_rachuje_biale += 1


print(biale_rachuje_czarne, czarne_rachuje_biale)
