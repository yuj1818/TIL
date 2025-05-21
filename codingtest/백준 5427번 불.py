from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    t = 0
    while pos:
        t += 1
        for _ in range(len(fire)):
            y, x = fire.popleft()
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    fire.append((ny, nx))
        for _ in range(len(pos)):
            y, x = pos.popleft()
            if y == 0 or x == 0 or y == h - 1 or x == w - 1: return t
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    pos.append((ny, nx))
    return 'IMPOSSIBLE'

tc = int(input())
for _ in range(tc):
    w, h = map(int, input().split())
    visited = [[0] * w for _ in range(h)]
    fire = deque()
    pos = deque()
    for i in range(h):
        for j, x in enumerate(input().strip()):
            if x != '.': visited[i][j] = 1
            if x == '*': fire.append((i, j))
            elif x == '@': pos.append((i, j))
    print(bfs())