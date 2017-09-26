#!python3

def bin_add(a, b):
    n = max(len(a), len(b))
    c = [0] * (n + 1)
    carry = 0
    for i in range(n-1, -1, -1):
        c[i+1] = (a[i] + b[i] + carry) % 2
        carry = (a[i] + b[i] + carry) // 2
    c[0] = carry
    
    return c

