import sys
input = sys.stdin.readline

def check(board):
    for row in board:
        if len(set(row)) < 9: return False
    return True

for tc in range(int(input())):
    if tc != 0: input()
    sudoku1 = [list(map(int, input().split())) for _ in range(9)]
    sudoku2 = list(zip(*sudoku1))
    sudoku3 = []

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            line = [sudoku1[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            sudoku3.append(line)

    if check(sudoku1) and check(sudoku2) and check(sudoku3):
        answer = "CORRECT"
    else:
        answer = "INCORRECT"

    print(f"Case {tc + 1}: {answer}")
