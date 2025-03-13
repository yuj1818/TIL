import sys
input = sys.stdin.readline
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def bfs(n):
    global t, cnt, size, sy, sx
    visited = [[0] * n for _ in range(n)]
    visited[sy][sx] = 1
    s = [(sy, sx)]
    ct = 0
    while s:
        ns = []
        cand = []
        ct += 1
        for cy, cx in s:
            for dy, dx in d:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and 0 <= grid[ny][nx] <= size:
                    ns.append((ny, nx))
                    visited[ny][nx] = 1
                    if 0 < grid[ny][nx] < size: cand.append((ny, nx))
        if cand:
            cand.sort(key=lambda x: (x[0], x[1]))
            sy, sx = cand[0]
            grid[sy][sx] = 0
            t += ct
            cnt += 1
            if cnt == size:
                cnt = 0
                size += 1
            return True
        s = ns
    return False

def main():
    global t, cnt, size, sy, sx, grid
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    sy, sx, size = 0, 0, 2
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 9:
                sy, sx = i, j
                grid[i][j] = 0
                break
    t, cnt = 0, 0
    while 1:
        if not bfs(n): break

    print(t)

if __name__ == '__main__':
    main()