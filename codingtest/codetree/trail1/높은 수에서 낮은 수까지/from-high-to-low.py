a, b = map(int, input().split())
if a < b: print(*range(b, a - 1, -1))
else: print(*range(a, b - 1, -1))