n, r, c = map(int, input().split())
b = [['.'] * n for _ in range(n)]
re = r % 2
ce = c % 2
for i in range(n):
    x = ce if re == i % 2 else (c + 1) % 2
    for j in range(x, n, 2):
        b[i][j] = 'v'
print('\n'.join([''.join(row) for row in b]))