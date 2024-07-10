def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, l, h):
    pivot = A[l]
    i = l
    j = h
    while i <= j:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i <= j:
            swap(A, i, j)
            i += 1
            j -= 1

    swap(A, l, j)
    return j

def quick_sort(A, l, h):
    if l < h:
        j = partition(A, l, h)
        quick_sort(A, l, j)
        quick_sort(A, l + 1, h)

A = [5,3,7,2,6,1,10]
quick_sort(A, 0, len(A) - 1)
print(A)

def qsort(A, l, h):
    if l >= h:
        return

    i = l
    j = h    
    pivot = A[l]

    while i <= j:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i <= j:
            swap(A, i, j)
            i += 1
            j += 1

    qsort(A, l, j)
    qsort(A, i, h)

A = [5,3,7,2,6,1,10]
qsort(A, 0, len(A) - 1)
print(A)
