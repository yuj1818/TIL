def bfs():
    while q:
        x, cnt = q.pop(0)
        if x == b: return cnt +1
        for nx in (x * 2, x * 10 + 1):
            if nx <= b: q.append((nx, cnt + 1))
    return -1

a, b = map(int, input().split())
q = [(a, 0)]
print(bfs())