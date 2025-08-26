import sys
s = int(sys.stdin.readline())
q = [(1, 0, 0)]
visited = set([(1, 0)])
while q:
    x, c, t = q.pop(0)
    if x == s:
        print(t)
        exit()
    for nx, nc in [(x, x), (x + c, c), (x - 1, c)]:
        if 0 <= nx < 1001 and 0 <= nc < 1001 and (nx, nc) not in visited:
            q.append((nx, nc, t + 1))
            visited.add((nx, nc))