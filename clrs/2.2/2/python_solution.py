#!python3

def selection_sort(a, n):
    for i in range(0, n):
        k = i #minimal value index for this row
        for j in range(i+1, n):
            if a[j] < a[k]:
                k = j
        if a[k] < a[i]:
            a[i], a[k] = a[k], a[i]
    return a
