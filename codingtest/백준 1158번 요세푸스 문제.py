n, k = map(int, input().split())
q = list(range(1, n + 1))
i = 0
print(f"<{', '.join(map(str, [q.pop(i := (i + k - 1) % len(q)) for _ in range(n)]))}>")