n = int(input())
print(' '.join(map(str, list(range(1, n + 1, 2)) + list(range(n - (1 if n % 2 else 0), 0, -2)))))
