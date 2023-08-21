T = int(input())
for tc in range(1, T + 1):
    k = int(input())
    n = int(input())
    apart = [[0] * n for _ in range(k + 1)]
    apart[0] = [i for i in range(1, n + 1)]
    for i in range(1, k + 1):
        for j in range(n):
            apart[i][j] = sum(apart[i - 1][:j + 1])
    print(apart[k][n - 1])