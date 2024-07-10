words = []
with open("Dane_PR2/sygnaly.txt") as f:
    lines = f.readlines()
    for line in lines:
        words.append(line.strip())

i = 1
concated = ""
for word in words:
    if i % 40 == 0:
        concated += word[9]
    i += 1
print("zad 4.1")
print(concated)

max_word = ""
max_letters = 0
for word in words:
    s = set()
    for c in word:
        s.add(c)
    if len(s) > max_letters:
        max_letters = len(s)
        max_word = word
print("zad 4.2")
print(max_word, max_letters)

print("zad 4.3")
count = 0
for word in words:
    s = set()
    for c in word:
        s.add(c)
    good = True
    for index, c1 in enumerate(s):
        for c2 in list(s)[index + 1:]:
            if ord(c1) - ord(c2) <= 10 and ord(c1) - ord(c2) >= -10:
                continue
            else:
                good = False
                break
    if good:
        count += 1
        print(word)
print(count)
