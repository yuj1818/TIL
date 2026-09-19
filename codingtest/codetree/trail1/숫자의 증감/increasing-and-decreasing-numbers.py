c, n = input().split()
n = int(n)
if c == 'A': print(*range(1, n + 1))
else: print(*range(n, 0, -1))