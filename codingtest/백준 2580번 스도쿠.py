import sys
input = sys.stdin.readline

def get_z_idx(y, x): return (y // 3) * 3 + x // 3

def get_nums(y, x):
    ny = Y[y]
    nx = X[x]
    nz = Z[get_z_idx(y, x)]
    nums = set()
    bnum = ny | nx | nz
    for i in range(1, 10):
        if (bnum >> i) & 1 == 0: nums.add(i)
    return nums

def find():
    if len(blank) == 0: return True
    blank.sort(key=lambda x: len(get_nums(*x)))
    y, x = blank[0]
    nums = get_nums(y, x)
    for num in nums:
        Y[y] |= (1 << num)
        X[x] |= (1 << num)
        Z[get_z_idx(y, x)] |= (1 << num)
        board[y][x] = num
        blank.remove((y, x))
        if find(): return True
        blank.append((y, x))
        Y[y] &= ~(1 << num)
        X[x] &= ~(1 << num)
        Z[get_z_idx(y, x)] &= ~(1 << num)
        board[y][x] = 0
    return False

board = [list(map(int, input().split())) for _ in range(9)]
blank = []
X = [0] * 9
Y = [0] * 9
Z = [0] * 9
for i in range(9):
    for j in range(9):
        if board[i][j] == 0: blank.append((i, j))
        else:
            Y[i] |= (1 << board[i][j])
            X[j] |= (1 << board[i][j])
            Z[get_z_idx(i, j)] |= (1 << board[i][j])
find()
for row in board:
    print(' '.join(map(str, row)))