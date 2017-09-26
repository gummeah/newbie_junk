#!python3

def bin_add(a, b):
    n = max(len(a), len(b))
    c = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        c[i+1] = c[i+1] + a[i] + b[i]
        if c[i+1] == 3:
            c[i+1] = 1 
            c[i] = 1
        elif c[i+1] == 2:
            c[i+1] = 0
           c[i] = 1

    return c
