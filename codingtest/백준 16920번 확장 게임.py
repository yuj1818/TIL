from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    sig = True
    while sig:
        sig = False
        for i in range(1, p + 1):
            if not pos[i]: continue
            q = pos[i]
            for _ in range(limit[i]):
                if not q: break
                for _ in range(len(q)):
                    y, x = q.popleft()
                    for dy, dx in dyx:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == '.':
                            board[ny][nx] = i
                            q.append((ny, nx))
                            sig = True
                            ans[i] += 1

dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m, p = map(int, input().split())
limit = [0] + list(map(int, input().split()))
board = []
pos = [deque() for i in range(p + 1)]
ans = [0] * (p + 1)
for i in range(n):
    row = list(input().strip())
    for j in range(m):
        v = row[j]
        if v != '.' and v != '#':
            pos[int(v)].append((i, j))
            ans[int(v)] += 1
    board.append(row)

bfs()
print(' '.join([str(ans[i]) for i in range(1, p + 1)]))