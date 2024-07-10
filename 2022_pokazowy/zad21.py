A = [0]

def tura(k):
    for i in range(s, A[k] - 1, -1):
        if B[i - A[k]] == 1 and B[i] == 0:
            B[i] = 1

s = int(input())
n = int(input())
for i in range(n):
    e = int(input())
    A.append(e)
    
B = [0 for x in range(0, s+1)]
B[0] = 1
for k in range(1, n+1):
    tura(k)

print(B[s] == 1)
