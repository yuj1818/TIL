m, n = map(int, input().split())
print(min(m, n) * 2 - (1 if m > n else 2))