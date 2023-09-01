directions = {
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],    # 상 하 좌 우
    2: [(-1, 0), (1, 0)],    # 상 하
    3: [(0, -1), (0, 1)],    # 좌 우
    4: [(-1, 0), (0, 1)],    # 상 우
    5: [(1, 0), (0, 1)],    # 하 우
    6: [(1, 0), (0, -1)],    # 하 좌
    7: [(-1, 0), (0, -1)]    # 상 좌
}
T = int(input())

def dfs(y, x, cnt):
    if cnt == L:
        return
    for d in directions[underground[y][x]]:
        nx = x + d[1]
        ny = y + d[0]
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and underground[ny][nx]:
            if tuple([-1 * pos for pos in d]) in directions[underground[ny][nx]]:
                visited[ny][nx] = 1
                dfs(ny, nx, cnt + 1)
                visited[ny][nx] = 0
                places.add((ny, nx))

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    places = set()
    places.add((R, C))
    dfs(R, C, 1)
    ans = len(places)
    print(f'#{tc} {ans}')