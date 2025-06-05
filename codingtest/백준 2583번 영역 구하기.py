import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def calc(y, x):
    paper[y][x] = 1
    res = 0
    s = [(y, x)]
    while s:
        y, x = s.pop()
        res += 1
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not paper[ny][nx]:
                s.append((ny, nx))
                paper[ny][nx] = 1
    return res

def main():
    global n, m, paper
    m, n, k = map(int, input().split())
    paper = [[0] * m for _ in range(n)]
    for _ in range(k):
        y1, x1, y2, x2 = map(int, input().split())
        for i in range(y1, y2):
            for j in range(x1, x2):
                paper[i][j] = 1
    cnt = 0
    size = []
    for i in range(n):
        for j in range(m):
            if not paper[i][j]:
                cnt += 1
                size.append(calc(i, j))
    print(cnt)
    print(*sorted(size))

if __name__ == '__main__':
    main()