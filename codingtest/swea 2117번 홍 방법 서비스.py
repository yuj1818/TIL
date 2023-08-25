T = int(input())
def calculate_profit(i, j):
    global max_home
    for k in range(1, N + 2):
        home = []
        expense = k * k + (k - 1) * (k - 1)
        for ni in [y for y in range(i - (k - 1), i + k) if 0 <= y < N]:
            for nj in [x for x in range(j - (k - 1), j + k) if 0 <= x < N]:
                if abs(i - ni) + abs(j - nj) <= k - 1:
                    if city[ni][nj] == 1:
                        home.append((i, j))
        profit = len(home) * M - expense
        if profit >= 0:
            max_home = max(max_home, len(home))

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    max_home = 0
    for i in range(N):
        for j in range(N):
            calculate_profit(i, j)
    print(f'#{tc} {max_home}')