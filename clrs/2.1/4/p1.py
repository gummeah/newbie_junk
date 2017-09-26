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
carry = 0
for i in range(n-1, -1, -1):
    c[i+1] = (a[i] + b[i] + carry) % 2
    carry = (a[i] + b[i] + carry) // 2
c[0] = carry

print(''.join(map(str, c)))
print("--- %s seconds ---" % (time.time() - start_time))
