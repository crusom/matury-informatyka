A = [0]
for x in range(5, 101, 5):
    A.append(x)

def tura(k):
    for i in range(s, A[k] - 1, -1):
        if B[i - A[k]] == 1 and B[i] == 0:
            B[i] = 1

s = 500
n = len(A) - 1 
B = [0 for x in range(0, s+1)]
B[0] = 1
for k in range(1, n+1):
    tura(k)

c = 0
for i in range(len(B)):
    if B[i] == 1:
        c+=1
print(c)

