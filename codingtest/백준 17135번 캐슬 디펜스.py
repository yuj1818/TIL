import sys
input = sys.stdin.readline

def calc(i, j, k):
    global ans, isOver
    cnt = 0
    killed = [0] * N
    for t in range(N):
        if cnt + (N - t) * 3 <= ans: break
        if cnt + rest[t] <= ans: break
        target = set()
        for pos in (i, j, k):
            for d, x, y in archer[pos]:
                if t > y or d - t > D or killed[y] & (1 << x): continue
                if (y, x) in target: break
                target.add((y, x))
                break
        for y, x in target:
            killed[y] |= (1 << x)
            cnt += 1
        if ans < cnt: ans = cnt
        if ans == MAX: isOver = True

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
rest = [0] * N
archer = [[] for _ in range(M)]
total = 0
for i in range(N):
    for j in range(M):
        if not board[i][j]: continue
        total += 1
        for p in range(M):
            archer[p].append((abs(i - N) + abs(j - p), j, N - 1 - i))
    rest[i] = total
rest = rest[::-1]
archer = list(map(lambda x: sorted(x), archer))
MAX = min(N * 3, total)
ans = 0
isOver = False
for i in range(M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            calc(i, j, k)
            if isOver:
                print(ans)
                sys.exit()
print(ans)