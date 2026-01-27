import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
ans = {-1: 0, 0: 0, 1: 0}

def dq(y, x, s):
    cur = paper[y][x]
    for i in range(y, y + s):
        for j in range(x, x + s):
            if paper[i][j] != cur:
                nxt = s // 3
                for k in range(3):
                    for l in range(3):
                        dq(y + (nxt * k), x + (nxt * l), nxt)
                return
    ans[cur] += 1
    return

dq(0, 0, n)
print('\n'.join(map(str, ans.values())))