import sys
input = sys.stdin.readline

def dfs(y, x, cnt, a_cnt):
    global ans
    if ans: return
    if a_cnt >= 2:
        ans = 1
        return
    if cnt == 3: return
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if 0 <= ny < 5 and 0 <= nx < 5 and board[ny][nx] != -1:
            prev = board[ny][nx]
            board[ny][nx] = -1
            dfs(ny, nx, cnt + 1, a_cnt + prev)
            board[ny][nx] = prev

board = [list(map(int, input().split())) for _ in range(5)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
r, c = map(int, input().split())
ans = 0
board[r][c] = -1
dfs(r, c, 0, 0)
print(ans)