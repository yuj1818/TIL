import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def main():
    n = int(input())
    seat = [[0] * n for _ in range(n)]
    empty = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for di, dj in d:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n: empty[ni][nj] += 1
    pos = [[] for _ in range(n ** 2 + 1)]
    likes = dict()
    for _ in range(n ** 2):
        s, *like = map(int, input().split())
        likes[s] = set(like)
        count = [[0] * n for _ in range(n)]
        a = []
        for f in like:
            if pos[f]:
                i, j = pos[f]
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and not seat[ni][nj]:
                        count[ni][nj] += 1
                        a.append((count[ni][nj], empty[ni][nj], ni, nj))
        if not a:
            for i in range(n):
                for j in range(n):
                    if not seat[i][j]: a.append((count[i][j], empty[i][j], i, j))
        a.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
        y, x = a[0][2], a[0][3]
        pos[s] = [y, x]
        seat[y][x] = s
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and empty[ny][nx]:
                empty[ny][nx] -= 1

    ans = 0
    score = [0, 1, 10, 100, 1000]
    for i in range(n):
        for j in range(n):
            cnt = 0
            for di, dj in d:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    if seat[ni][nj] in likes[seat[i][j]]: cnt += 1
            ans += score[cnt]
    print(ans)

main()