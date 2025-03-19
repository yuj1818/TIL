import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = 0

def move(board):
    for i in range(len(board)):
        tmp = []
        v = 0
        for x in board[i]:
            if x == 0: continue
            elif v != x:
                if v == 0: v = x
                elif v != 0:
                    tmp.append(v)
                    v = x
            elif v == x:
                tmp.append(v * 2)
                v = 0
        if v: tmp.append(v)
        board[i] = tmp + ([0] * (n - len(tmp)))

def dfs(d, board):
    global res
    if d == 5:
        mv = max(map(max, board))
        if res < mv: res = mv
        return

    cboard = [row[::] for row in board]
    move(cboard)
    dfs(d + 1, cboard)

    cboard = [row[::-1] for row in board]
    move(cboard)
    dfs(d + 1, cboard)

    zboard = list(map(list, zip(*board)))
    cboard = [row[::] for row in zboard]
    move(cboard)
    dfs(d + 1, cboard)

    cboard = [row[::-1] for row in zboard]
    move(cboard)
    dfs(d + 1, cboard)

dfs(0, board)
print(res)