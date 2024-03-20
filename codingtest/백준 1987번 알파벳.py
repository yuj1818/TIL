import sys
input = sys.stdin.readline

def dfs(s, cnt):
    global max_cnt
    max_cnt = max(cnt, max_cnt)

    for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
        ny = s[0] + dy
        nx = s[1] + dx

        if 0 <= ny < R and 0 <= nx < C and not alpha[board[ny][nx]]:
            alpha[board[ny][nx]] = True
            dfs((ny, nx), cnt + 1)
            alpha[board[ny][nx]] = False

R, C = map(int, input().split())
board = [list(map(lambda x:ord(x)-65, input())) for _ in range(R)]
alpha = [False] * 26
alpha[board[0][0]] = True
max_cnt = 1
dfs((0, 0), 1)
print(max_cnt)
