import sys
input = sys.stdin.readline
message = input().strip()
key = input().strip()
alpha = dict()
board = [['.'] * 5 for _ in range(5)]
for x in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
    alpha[x] = tuple()
r, c = 0, 0
for x in key:
    if alpha[x]: continue
    alpha[x] = (r, c)
    board[r][c] = x
    c += 1
    if c == 5:
        r += 1
        c = 0
for x in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
    if alpha[x]: continue
    alpha[x] = (r, c)
    board[r][c] = x
    c += 1
    if c == 5:
        r += 1
        c = 0

pairs = ['']
for x in message:
    if pairs[-1] and pairs[-1][-1] == x:
        if pairs[-1][0] == 'X':
            pairs[-1] += 'Q'
        else:
            pairs[-1] += 'X'
        pairs.append(x)
    else:
        pairs[-1] += x
        if len(pairs[-1]) == 2: pairs.append('')
if pairs[-1]:
    if len(pairs[-1]) == 1: pairs[-1] += 'X'
else: pairs.pop()

ans = ''
for f, b in pairs:
    fy, fx = alpha[f]
    by, bx = alpha[b]
    if fy == by:
        ans += board[fy][(fx + 1) % 5] + board[by][(bx + 1) % 5]
    elif fx == bx:
        ans += board[(fy + 1) % 5][fx] + board[(by + 1) % 5][bx]
    else:
        ans += board[fy][bx] + board[by][fx]

print(ans)