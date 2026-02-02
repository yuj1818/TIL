import sys

MAX = 1000000
s = [1] * (MAX + 1)
s[0] = s[1] = 0
for i in range(2, int(MAX**0.5) + 1):
    if s[i]:
        for k in range(i * i, MAX + 1, i):
            s[k] = 0
for n in sys.stdin.readlines():
    n = int(n)
    if n == 0:
        break
    for i in range(3, int(n / 2) + 1, 2):
        if s[i] and s[n - i]:
            print(f"{n} = {i} + {n - i}")
            break
    else:
        print('Goldbach\'s conjecture is wrong.')
