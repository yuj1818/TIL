import sys
input = sys.stdin.readline

def check(board):
    for row in board:
        if len(set(row)) < 9: return False
    return True

for tc in range(int(input())):
    if tc != 0: input()
    board = [list(map(int, input().split())) for _ in range(9)]
    zboard = list(zip(*board))
    sboard = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            line = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            sboard.append(line)
    print(f"Case {tc + 1}: {'CORRECT' if check(board) and check(zboard) and check(sboard) else 'INCORRECT'}")