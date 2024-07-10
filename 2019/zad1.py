def szukaj_bin(A):
    l = 0
    p = len(A) - 1
    while l < p:
        s = (l + p) // 2
        if A[s] % 2 != 0:
            l = s + 1
        else:
            p = s
    return A[p]

A = [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]
print(szukaj_bin(A))
