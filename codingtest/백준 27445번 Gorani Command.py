n, m = map(int, input().split())
cols = [int(input()) for _ in range(n - 1)]
rows = list(map(int, input().split()))
cols.append(rows[0])
print(cols.index(min(cols)) + 1, rows.index(min(rows)) + 1)