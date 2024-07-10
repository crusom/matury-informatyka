def tura(A, k):
    for i in range(s, A[k] - 1, -1):
        if B[i - A[k]] == 1 and B[i] == 0:
            B[i] = 1


A = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
n = len(A) - 1 
for i in range(1, 200+1):
    s = i
    B = [0 for x in range(0, s+1)]
    B[0] = 1
    for k in range(1, n+1):
        tura(A,k)
    if B[s] != 1:
        print("CHUJ")
