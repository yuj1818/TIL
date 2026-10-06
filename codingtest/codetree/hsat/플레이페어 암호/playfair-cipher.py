s = input()
k = input()
n = len(k)
board = [[''] * 5 for _ in range(5)]
used = set()
pos = dict()
i, j = 0, 0
for x in k:
    if x in used: continue
    used.add(x)
    pos[x] = (i, j)
    board[i][j] = x
    j += 1
    if j >= 5:
        i += 1
        j = 0
for idx in range(65, 91):
    if board[-1][-1] != '': break
    if idx == 74: continue
    x = chr(idx)
    if x in used:continue
    used.add(x)
    pos[x] = (i, j)
    board[i][j] = x
    j += 1
    if j >= 5:
        i += 1
        j = 0
fairs = [[]]
for x in s:
    if len(fairs[-1]) == 2: fairs.append([])
    if not fairs[-1] or fairs[-1][0] != x: fairs[-1].append(x)
    else:
        if fairs[-1][0] == 'X': fairs[-1].append('Q')
        else: fairs[-1].append('X')
        fairs.append([x])
if len(fairs[-1]) == 1: fairs[-1].append('X')
ans = ''
for a, b in fairs:
    ay, ax = pos[a]
    by, bx = pos[b]
    if ay == by:
        na = board[ay][(ax + 1) % 5]
        nb = board[by][(bx + 1) % 5]
    elif ax == bx:
        na = board[(ay + 1) % 5][ax]
        nb = board[(by + 1) % 5][bx]
    else:
        na = board[ay][bx]
        nb = board[by][ax]
    ans += na + nb
print(ans)