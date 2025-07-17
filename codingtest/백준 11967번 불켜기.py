import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def main():
    n, m = map(int, input().split())
    s = dict()
    for _ in range(m):
        x, y, a, b = map(lambda x: int(x) - 1, input().split())
        if s.get((x, y)): s[(x, y)].append((a, b))
        else: s[(x, y)] = [(a, b)]
    ans = 1
    q = [(0, 0)]
    room = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    room[0][0] = 1
    visited[0][0] = 1
    while q:
        y, x = q.pop(0)
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and room[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = 1
        if not s.get((y, x)): continue
        for ny, nx in s[(y, x)]:
            if room[ny][nx]: continue
            room[ny][nx] = 1
            ans += 1
            for dy, dx in d:
                if 0 <= ny + dy < n and 0 <= nx + dx < n and visited[ny + dy][nx + dx]:
                    q.append((ny, nx))
                    visited[ny][nx] = 1
                    break
    print(ans)

main()