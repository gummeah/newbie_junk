#!python3
import time
a = input()
b = input()
print(a, b)
a = [int(i) for i in a]
b = [int(i) for i in b]
n = max(len(a), len(b))
c = [0] * (n + 1)
start_time = time.time()
for i in range(n-1, -1, -1):
    c[i+1] = c[i+1] + a[i] + b[i]
    if c[i+1] == 3:
        c[i+1] = 1 
        c[i] = 1
    elif c[i+1] == 2:
        c[i+1] = 0
        c[i] = 1

print(''.join(map(str, c)))
print("--- %s seconds ---" % (time.time() - start_time))
