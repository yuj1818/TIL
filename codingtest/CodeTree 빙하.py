def find_zero():
    zero = []
    q = deque([(0, 0)])
    visited = [[0] * (m + 2) for _ in range(n + 2)]
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n + 2 and 0 <= nx < m + 2) or visited[ny][nx]: continue
            if a[ny][nx]:
                zero.append((y, x))
                continue
            visited[ny][nx] = 1
            q.append((ny, nx))
    return zero

from collections import deque
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
a = [[0] * (m + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (m + 2)]
t, last = 0, 0
while 1:
    zero = deque(find_zero())
    if not zero: break
    melted = 0
    while zero:
        y, x = zero.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < m) or not a[ny][nx]: continue
            melted += 1
            a[ny][nx] = 0
    t += 1
    last = melted
print(t, last)
