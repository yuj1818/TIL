import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    MIN = -100 * n * m
    board = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, m):
        board[0][i] += board[0][i - 1]
    for i in range(1, n):
        c1 = []
        c2 = []
        for j in range(m):
            c1.append(max(board[i - 1][j], (c1[-1] if j else MIN)) + board[i][j])
            c2.append(max(board[i - 1][-j - 1], (c2[-1] if j else MIN)) + board[i][-j - 1])
        for j in range(m):
            board[i][j] = max(c1[j], c2[-j - 1])
    print(board[n - 1][m - 1])

main()