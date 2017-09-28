#!python3

def selection_sort(a):
    n = len(a)
    for i in range(0, n-1):
        k = i #minimal value index for this row
        for j in range(i+1, n):
            if a[j] < a[k]:
                k = j
        if a[k] < a[i]:
            a[i], a[k] = a[k], a[i]
    return a
