string = []
max_ciag = 0
cur_ciag = 0
cur_ciag_rodz = ""
max_ciag_rodz = ""
max_letter = 30 * [0]
letter = ''
with open("DANE_2105/instrukcje.txt", "r") as f:
    for line in f:
        words = line.split()
        op = words[0]
        val = words[1]
        #print(val)
        if op == "DOPISZ":
            string += val
            max_letter[ord(val) - ord('A')] += 1
        elif op == "USUN":
            string.pop()
        elif(op == "ZMIEN"):
            string[len(string) - 1] = val
        elif(op == "PRZESUN"):
            for i in range(len(string)):
                if(string[i] == val):
                    if(val == 'Z'):
                        string[i] = 'A'
                    else:
                        string[i] = chr(ord(val) + 1)
                    break
        
        if(cur_ciag_rodz == op):
            cur_ciag += 1
        else:
            if(cur_ciag > max_ciag):
                max_ciag = cur_ciag
                max_ciag_rodz = cur_ciag_rodz
            cur_ciag_rodz = op
            cur_ciag = 1


print("4.1: " + str(len(string)))
print("4.2: " + str(max_ciag_rodz) + " " + str(max_ciag))
tmp = 0
tmp_max = 0
for i in range(len(max_letter)):
    if max_letter[i] > tmp_max:
        tmp_max = max_letter[i]
        tmp = i
print("4.3: " + chr(ord('A') + tmp) + " " + str(tmp_max))
print("4.4: " + ''.join(string))
