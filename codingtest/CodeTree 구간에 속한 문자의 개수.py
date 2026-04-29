n, m, k = map(int, input().split())
grid = [input() for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(k)]
acc = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(3)]
for c in range(3):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            acc[c][i][j] = acc[c][i - 1][j] + acc[c][i][j - 1] - acc[c][i - 1][j - 1]
            if ord(grid[i - 1][j - 1]) - 97 == c: acc[c][i][j] += 1
for r1, c1, r2, c2 in queries:
    for i in range(3):
        print(acc[i][r2][c2] - acc[i][r1 - 1][c2] - acc[i][r2][c1 - 1] + acc[i][r1 - 1][c1 - 1], end=' ')
    print()
