import sys
input = sys.stdin.readline
a, b = map(int, input().split())
q = [(a, 0)] + [(int(input()), 1) for _ in range(int(input()))]
visited = [float('inf')] * 1001
while q:
    x, cnt = q.pop(0)
    if x == b:
        print(cnt)
        sys.exit()
    visited[x] = 1
    for nx in (x + 1, x - 1):
        if 0 < nx < 1001 and visited[nx] > cnt + 1:
            q.append((nx, cnt + 1))
            visited[nx] = cnt + 1