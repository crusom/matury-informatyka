'''
Tak działa, krok po kroku, algorytm wyszukiwania binarnego w przypadku gry w zgadywanie liczb:

    Niech min=1, max = n 
    Wyznacz średnią z  max i min zaokrąglając w dół do liczby całkowitej.
    Jeśli odgadłeś liczbę, stop. Znalazłeś ją!
    Jeśli twoja liczba była zbyt mała, ustaw zmienną min, aby była od niej o jeden większa.
    Jeśli twoja liczba była zbyt wysoka, ustaw zmienną max, aby była od niej o jeden mniejsza.
    Wróć do kroku numer 2.
'''

# to jest do zadania Zadania 1.1 z matury 2019, polecam obczaić, bo binary search się może przydać
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
