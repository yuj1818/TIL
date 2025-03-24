import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(i, j):
    global idx
    visited[i][j] = -1
    q = [(i, j)]
    idx += 1
    cnt = 1
    rainbow = 0
    while q:
        r, c = q.pop(0)
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] != -1 and visited[nr][nc] != idx:
                if grid[nr][nc] == grid[i][j]:
                    visited[nr][nc] = -1
                    q.append((nr, nc))
                    cnt += 1
                elif grid[nr][nc] == 0:
                    visited[nr][nc] = idx
                    q.append((nr, nc))
                    rainbow += 1
                    cnt += 1
    if cnt > 1: blocks.append((cnt, rainbow, i, j))

def remove(i, j, num):
    grid[i][j] = -2
    q = [(i, j)]
    while q:
        r, c = q.pop(0)
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (grid[nr][nc] == 0 or grid[nr][nc] == num):
                grid[nr][nc] = -2
                q.append((nr, nc))

def gravity():
    for j in range(n):
        idx = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j] == -1:
                idx = i - 1
            elif grid[i][j] >= 0:
                v = grid[i][j]
                grid[i][j] = -2
                grid[idx][j] = v
                idx -= 1

def main():
    global idx, grid, blocks, visited, n
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    score = 0
    while 1:
        visited = [[0] * n for _ in range(n)]
        blocks = []
        idx = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    bfs(i, j)
        if blocks:
            blocks.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
            cnt, rainbow, i, j = blocks[0]
            score += cnt ** 2
            remove(i, j, grid[i][j])
        else: break
        gravity()
        grid = list(map(list, zip(*grid)))[::-1]
        gravity()
    print(score)

main()