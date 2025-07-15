import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def main():
    n, m = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(n)]
    cheese[0][0] = -1
    q = [(0, 0)]
    t = -1
    while q:
        nq = []
        while q:
            y, x = q.pop(0)
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m:
                    if cheese[ny][nx] < 0: continue
                    if cheese[ny][nx] == 0:
                        q.append((ny, nx))
                        cheese[ny][nx] = -1
                    elif cheese[ny][nx] == 1:
                        cheese[ny][nx] += 1
                    else:
                        nq.append((ny, nx))
                        cheese[ny][nx] = -1
        q = nq
        t += 1
    print(t)

main()