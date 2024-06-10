from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = [0] * 101
visited = [0] * 101
ladders = dict()
snakes = dict()

for _ in range(n):
    x, y = map(int, input().split())
    ladders[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snakes[u] = v

q = deque([1])

while q:
    x = q.popleft()
    if x == 100:
        print(cnt[x])
        break

    for i in range(1, 7):
        nxt = x + i
        if nxt > 100:
            break

        if ladders.get(nxt):
            nxt = ladders[nxt]

        if snakes.get(nxt):
            nxt = snakes[nxt]

        if not visited[nxt]:
            visited[nxt] = 1
            cnt[nxt] = cnt[x] + 1
            q.append(nxt)