import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0)]

def rotate(box):
    return [list(x[::-1]) for x in zip(*box)]

def control(board):
    nboard = [row[::] for row in board]
    h = len(board)
    for i in range(h):
        for j in range(len(board[i])):
            for di, dj in d:
                ni, nj = i + di, j + dj
                if not (0 <= ni < h and 0 <= nj < len(board[ni])): continue
                diff = abs(board[i][j] - board[ni][nj]) // 5
                if diff > 0:
                    if board[i][j] > board[ni][nj]:
                        nboard[i][j] -= diff
                        nboard[ni][nj] += diff
                    else:
                        nboard[i][j] += diff
                        nboard[ni][nj] -= diff
    return nboard

def flatten(board):
    nboard = []
    h, w = len(board), len(board[-1])
    for j in range(w):
        for i in range(h - 1, -1, -1):
            if j < len(board[i]): nboard.append(board[i][j])
    return nboard

def main():
    n, k = map(int, input().split())
    board = list(map(int, input().split()))
    cnt = 0
    while max(board) - min(board) > k:
        min_v = min(board)
        for i in range(n):
            if board[i] == min_v: board[i] += 1
        board = [[board[0]], board[1:]]
        while 1:
            rb = rotate(board)
            if len(rb[0]) > len(board[-1]) - len(rb): break
            board = [*rb, board[-1][len(rb):]]
        board = control(board)
        board = flatten(board)
        l = len(board) // 2
        nboard = [board[:l][::-1], board[l:]]
        l //= 2
        tmp = rotate(rotate([nboard[0][:l], nboard[1][:l]]))
        board = tmp + [nboard[0][l:], nboard[1][l:]]
        board = control(board)
        board = flatten(board)
        cnt += 1
    print(cnt)

main()