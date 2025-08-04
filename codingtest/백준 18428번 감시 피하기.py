from itertools import combinations
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    for y, x in T:
        for dy, dx in d:
            ny, nx = y, x
            while 0 <= ny + dy < n and 0 <= nx + dx < n:
                ny += dy
                nx += dx
                if board[ny][nx] == 'O': break
                if board[ny][nx] == 'S': return False
    return True

def main():
    global board, n, T
    n = int(input())
    board = [input().strip().split() for _ in range(n)]
    T, S, X = [], [], []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'T': T.append((i, j))
            elif board[i][j] == 'S': S.append((i, j))
            else: X.append((i, j))
    for comb in combinations(X, 3):
        for y, x in comb: board[y][x] = 'O'
        if bfs():
            print('YES')
            sys.exit()
        for y, x in comb: board[y][x] = 'X'
    print('NO')

main()