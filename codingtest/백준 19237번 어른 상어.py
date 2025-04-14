import sys
input = sys.stdin.readline
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

def main():
    n, m, k = map(int, input().split())
    board = []
    shark = [[] for _ in range(m + 1)]
    for i in range(n):
        row = list(map(int, input().split()))
        board.append([])
        for j in range(n):
            board[-1].append([row[j], 0])
            if row[j]: shark[row[j]] = [i, j, 0]
    cur = list(map(int, input().split()))
    for i in range(m): shark[i + 1][-1] = cur[i]
    dseqs = [[[] for _ in range(5)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, 5):
            dseqs[i][j] = list(map(int, input().split()))
    total = m
    for t in range(1, 1001):
        pos = [[0] * n for _ in range(n)]
        for i in range(1, m + 1):
            if not shark[i]: continue
            si, sj, sd = shark[i]
            cand = []
            for d in dseqs[i][sd]:
                ny, nx = si + dy[d], sj + dx[d]
                if 0 <= ny < n and 0 <= nx < n:
                    if board[ny][nx][0] == 0 or board[ny][nx][1] < t - k:
                        if pos[ny][nx]:
                            shark[i].clear()
                            total -= 1
                        else:
                            pos[ny][nx] = i
                            shark[i] = [ny, nx, d]
                        break
                    elif not cand and board[ny][nx][0] == i:
                        cand = [ny, nx, d]
            else:
                ny, nx, d = cand
                if pos[ny][nx]:
                    shark[i].clear()
                    total -= 1
                else:
                    pos[ny][nx] = i
                    shark[i] = [ny, nx, d]
        for i in range(n):
            for j in range(n):
                if pos[i][j]: board[i][j] = [pos[i][j], t]
        if total == 1:
            return t
    return -1

print(main())