import sys
input = sys.stdin.readline
ans = dict()
for idx, x in enumerate('ABCDEFGHIJKLMNO'):
    ans[x] = (idx // 4, idx % 4)
puzzle = [input().rstrip() for _ in range(4)]
res = 0
for i in range(4):
    for j in range(4):
        if puzzle[i][j] == '.': continue
        ai, aj = ans[puzzle[i][j]]
        if (ai, aj) != (i, j):
            res += abs(ai - i) + abs(aj - j)
print(res)