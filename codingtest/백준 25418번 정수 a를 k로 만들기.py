from collections import deque
a, k = map(int, input().split())
q = deque([(a, 0)])
visited = {a}
while q:
    x, cnt = q.popleft()
    if x == k:
        print(cnt)
        break
    for nx in [x + 1, x * 2]:
        if nx <= k and nx not in visited:
            q.append((nx, cnt + 1))
            visited.add(nx)
